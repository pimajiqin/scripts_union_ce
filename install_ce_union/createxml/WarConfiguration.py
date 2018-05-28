#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: 陈二狗

import xml.dom.minidom

from conf.config import *
from mkpath import *


#生成xml文件
def WarConfiguration(channel, sid, CsIp, CsDbName, CsDbUser, CsDbPw):

    xmlpath = xml_path + '%s/%s/WarConfiguration.xml' % (channel, sid)
    mkdir(xml_path + channel + sid)

    impl = xml.dom.minidom.getDOMImplementation()
    #设置根结点configuration
    dom = impl.createDocument(None, 'configuration', None)
    root = dom.documentElement

    #设置2级节点
    employee1 = dom.createElement('environments')
    employee2 = dom.createElement('mappers')
    #增加属性
    employee1.setAttribute("default","ncp")
    root.appendChild(employee1)
    root.appendChild(employee2)
    #设置子结点 子节点添加属性
    name3A=dom.createElement('environment')
    name3A.setAttribute("id","ncp")
    employee1.appendChild(name3A)

    # 4A
    name4A=dom.createElement('transactionManager')
    name4A.setAttribute("type","JDBC")
    name3A.appendChild(name4A)

    # 4B
    name4B=dom.createElement('dataSource')
    name4B.setAttribute("type","POOLED")
    name3A.appendChild(name4B)

    # 5A
    name5A=dom.createElement('property')
    name5A.setAttribute("name", "driver")
    name5A.setAttribute("value", "com.mysql.jdbc.Driver")
    name4B.appendChild(name5A)

    # 5B
    name5B=dom.createElement('property')
    name5B.setAttribute("name", "url")
    name5B.setAttribute("value", "jdbc:mysql://%s:3306/%s?autoReconnect=true&amp;useUnicode=true&amp;characterEncoding=utf8" % (CsIp, CsDbName))
    name4B.appendChild(name5B)

    # 5C
    name5C=dom.createElement('property')
    name5C.setAttribute("name", "username")
    name5C.setAttribute("value", CsDbUser)
    name4B.appendChild(name5C)

    # 5D
    name5D=dom.createElement('property')
    name5D.setAttribute("name", "password")
    name5D.setAttribute("value", CsDbPw)
    name4B.appendChild(name5D)

    #3B1
    name3B1=dom.createElement('mapper')
    name3B1.setAttribute("resource","com/ft/ncp/dao/AllyWarAllyInfoMapper.xml")
    employee2.appendChild(name3B1)

    #3B2
    name3B2=dom.createElement('mapper')
    name3B2.setAttribute("resource","com/ft/ncp/dao/AllyWarWarInfoMapper.xml")
    employee2.appendChild(name3B2)

    #3B3
    name3B3=dom.createElement('mapper')
    name3B3.setAttribute("resource","com/ft/ncp/dao/AllyWarSeasonInfoMapper.xml")
    employee2.appendChild(name3B3)

    f= open(xmlpath, 'w') #w替换为a，追加
    dom.writexml(f, addindent='    ', newl='\n',  encoding = 'utf-8',)
    f.close()

    fp = file(xmlpath)
    lines = []
    for line in fp:
        lines.append(line)
    fp.close()

    lines.insert(1, '<!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN" "http://mybatis.org/dtd/mybatis-3-config.dtd">\n')  # 在第二行插入
    s = ''.join(lines)
    fp = file(xmlpath, 'w')
    fp.write(s)
    fp.close()

    print "WarConfiguration.xml 创建"
