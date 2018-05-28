#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: 陈二狗

import commands
import socket
import sys
import threading
import time

from conf.config import *
from install_ce_union.createxml.createallxml import *
from install_ce_union.sshcmd.paramiko_ssh import *
from install_ce_union.dboper.dbopertion import *

def echo_yellow(msg):
    print ' \033[1;33m %s \033[0m' % msg

def echo_red(msg):
    print ' \033[1;31m %s \033[0m' % msg

def checkport(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        echo_yellow('port %s OK!' % port)
        return True
    except:
        echo_yellow('port %s CLOSED!' % port)
        return False

def get_newpack(csv_source, csv_dest, jar_source, jar_dest):
    """ 从alpha服获取更新文件 """
    commands.getoutput("rsync -az %s:%s/* %s" % (alphaip, csv_source, csv_dest))
    commands.getoutput("rsync -az %s:%s/* %s" % (alphaip, jar_source, jar_dest))


def update_logic(channel, Ip, ServerId):
    """ 更新 """
    # 传cfg jar
    commands.getoutput("rsync -az %s/%s/logic/csvData/* %s:/opt/app/service%s/logic/cfg/csvData/" % (update_path, channel, Ip, ServerId))
    commands.getoutput("rsync -az %s/%s/logic/release/* %s:/opt/app/service%s/logic/lib/release/" % (update_path, channel, Ip, ServerId))
    echo_yellow("渠道 %s 逻辑服 %s 传cfg jar完成 " % (channel, ServerId))


def stop_logic(Ip, ServerId):

    U = SCP_SSH(Ip)
    U.ssh('bash /opt/app/service%s/logic/app.sh stop' % ServerId)
    echo_yellow("停止%s logic进程" % ServerId)

def restart_logic(Ip, ServerId):

    U = SCP_SSH(Ip)
    U.ssh('bash /opt/app/service%s/logic/app.sh restart' % ServerId)
    echo_yellow("启动%s logic完成" % ServerId)

def update_logic_all(channel, config):
    """ 更新所有文件 """
    for i in select_serverid_ip(config):
        t = threading.Thread(target=update_logic, args=(channel,i['Ip'],i['ServerId']))
        t.start()
    t.join()

def stop_logic_all(config):
    """ 更新所有文件 """
    for i in select_serverid_ip(config):
        t = threading.Thread(target=stop_logic, args=(i['Ip'],i['ServerId']))
        t.start()
    t.join()

def restart_logic_all(config):
    """ 更新所有文件 """
    for i in select_serverid_ip(config):
        t = threading.Thread(target=restart_logic, args=(i['Ip'], i['ServerId']))
        t.start()
    t.join()

def checkport_all(config):
    """ 更新所有文件 """
    for i in select_serverid_ip(config):
        t = threading.Thread(target=checkport, args=(natip, i['NatPort']))
        t.start()
    t.join()


configlist = []
paralist = sys.argv
paralist.remove(sys.argv[0])

if len(paralist) <> 2:
    echo_yellow("请输入正确的参数 eg: python deploy.py [all/a/b] [stop/update/restart]")
    sys.exit()

if sys.argv[0] == "all":
    configlist = [configa, configb]
elif sys.argv[0] == "a":
    configlist = [configa,]
elif sys.argv[0] == "b":
    configlist = [configb,]
else:
    echo_yellow("请输入正确的参数 eg: python deploy.py [all/a/b] [stop/update/restart]")
    sys.exit()

if __name__ == "__main__":
    starttime = time.time()

    if sys.argv[1] == "stop":
        for i in configlist:
            stop_logic_all(i)
        time.sleep(10)
        for i in configlist:
            checkport_all(i)
    elif sys.argv[1] == "update":
        for i in configlist:
            if i == configa:
                channel = 'a'
            else:
                channel = 'b'
            update_logic_all(channel, i)
    elif sys.argv[1] == "restart":
        for i in configlist:
            restart_logic_all(i)
        time.sleep(60)
        for i in configlist:
            checkport_all(i)
    else:
        echo_yellow("请输入正确的参数 eg: python deploy.py [all/a/b] [stop/update/restart]")
        sys.exit()

    endtime = time.time()
    print(endtime - starttime)
