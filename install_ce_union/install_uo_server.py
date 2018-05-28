#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: 陈二狗

import commands
import os
import sys
import time

from conf.config import *
from createxml.createallxml import *
from sshcmd.paramiko_ssh import *


def echo_yellow(msg):
    print 'This is a \033[1;33m %s \033[0m!' % msg

def echo_red(msg):
    print 'This is a \033[1;31m %s \033[0m!' % msg

def file_name(xml_path):
    """ 列出有所有xml """
    L = []
    for root, dirs, files in os.walk(xml_path):
        for file in files:
            if os.path.splitext(file)[1] == '.xml':
                L.append(os.path.join(root, file))
    return L

def deploy_new_server(channel, config, sid):
    """ 部署新服 """

    # 获取新服信息
    serverinfo = select_logic_info(config, sid)
    Ip = serverinfo['Ip']
    ServerId = serverinfo['ServerId']
    DbRootPw = serverinfo['DbRootPw']
    DbName = serverinfo['DbName']
    DbUser = serverinfo['DbUser']
    DbPw = serverinfo['DbPw']
    DbRUser = serverinfo['DbRUser']
    DbRPw = serverinfo['DbRPw']

    U = SCP_SSH(Ip)
    # 创建xml文件
    creat_all_xml(channel, config, ServerId)
    echo_yellow("创建xml文件")
    # 新建目录
    print U.ssh('mkdir -pv /opt/app/service%s' % ServerId)
    echo_yellow("新建目录service%s" % ServerId)
    # 传logic
    print commands.getoutput("rsync -az %s %s:/opt/app/service%s" % (source_logic_path, Ip, ServerId))
    echo_yellow("logic 移动到指定目录")
    # 传cfg jar
    print commands.getoutput("rsync -az %s%s/logic/csvData/* %s:/opt/app/service%s/logic/cfg/csvData/" % (update_path, channel, Ip, ServerId))
    print commands.getoutput("rsync -az %s%s/logic/release/* %s:/opt/app/service%s/logic/lib/release/" % (update_path, channel, Ip, ServerId))
    echo_yellow("传cfg jar")
    # 传xml到指定目录
    commands.getoutput("rsync -avz %s%s/* %s:/opt/app/service%s/logic/cfg" % (xml_path, channel,Ip, ServerId))
    echo_yellow("传xml到指定目录")
    # 创建数据库
    print U.ssh("%s%s%s%s%s" % ('/usr/local/mysql/bin/mysql -uroot -p', DbRootPw, ' -e "create database ', DbName, ';"'))
    echo_yellow("创建数据库")
    # 账号赋权
    print U.ssh("%s%s%s%s%s%s%s%s%s" % ("/usr/local/mysql/bin/mysql -uroot -p", DbRootPw, ' -e "grant all privileges on ', DbName, ".* to ", DbUser, "@'127.0.0.1' identified by '", DbPw, '\';"'))
    print U.ssh("%s%s%s%s%s%s%s%s%s" % ("/usr/local/mysql/bin/mysql -uroot -p", DbRootPw, ' -e "grant all privileges on ', DbName, ".* to ", DbUser, "@'172.24.%' identified by '", DbPw, '\';"'))
    print U.ssh("%s%s%s%s%s%s%s%s%s" % ("/usr/local/mysql/bin/mysql -uroot -p", DbRootPw, ' -e "grant all privileges on ', DbName, ".* to ", DbRUser, "@'%' identified by '", DbRPw, '\';"'))
    echo_yellow("账号赋权")
    # 导入表结构
    print commands.getoutput("/usr/bin/mysql -u%s -p%s -h%s %s< %s" % (DbUser, DbPw, Ip, DbName, create_logicdb_path))
    echo_yellow("导入表结构")
    # 初始化数据
    print U.ssh('bash /opt/app/service%s/logic/initData.sh start' % ServerId)
    echo_yellow("初始化数据完成")
    time.sleep(60)
    # 查询插入数据
    robot = select_arena_rank_info(Ip, DbUser, DbPw, DbName)
    if robot == 3500:
        echo_yellow("插入数据成功")
    else:
        echo_red("初始化失败，请检查")
        sys.exit()
    # 启动logic
    print U.ssh('bash /opt/app/service%s/logic/app.sh restart' % ServerId)
    echo_yellow("启动logic完成")


# 外部传参
paralist = sys.argv
paralist.remove(sys.argv[0])

if len(paralist) <> 2:
    echo_red("请输入正确的参数 eg: python install_uo_server.py [a/b] [serverid]")
    sys.exit()

if sys.argv[0] == "a":
    channel = "a"
    config = configa
elif sys.argv[0] == "b":
    channel = "b"
    config = configb
else:
    echo_red("请输入正确的参数 eg: python install_uo_server.py [a/b] [serverid]")
    sys.exit()

logicid = sys.argv[1]

if __name__ == '__main__':
    deploy_new_server(channel, config, logicid)