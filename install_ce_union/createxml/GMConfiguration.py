#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: 陈二狗

import xml.dom.minidom

from conf.config import *
from mkpath import *


#生成xml文件
def GMConfiguration(channel, sid, AccountIP, AccountDbName, AccountDbUser, AccountDbPw):

    xmlpath = xml_path + '%s/%s/GMConfiguration.xml' % (channel,sid)
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
    name5B.setAttribute("value", "jdbc:mysql://%s:3306/%s?autoReconnect=true&amp;useUnicode=true&amp;characterEncoding=utf8" % (AccountIP, AccountDbName))
    name4B.appendChild(name5B)

    # 5C
    name5C=dom.createElement('property')
    name5C.setAttribute("name", "username")
    name5C.setAttribute("value", AccountDbUser)
    name4B.appendChild(name5C)

    # 5D
    name5D=dom.createElement('property')
    name5D.setAttribute("name", "password")
    name5D.setAttribute("value", AccountDbPw)
    name4B.appendChild(name5D)

    #3B1
    name3B1=dom.createElement('mapper')
    name3B1.setAttribute("resource","com/ft/ncp/dao/DailyTotalServerMapper.xml")
    employee2.appendChild(name3B1)

    #3B2
    name3B2=dom.createElement('mapper')
    name3B2.setAttribute("resource","com/ft/ncp/dao/OrderListMapper.xml")
    employee2.appendChild(name3B2)

    #3B3
    name3B3=dom.createElement('mapper')
    name3B3.setAttribute("resource","com/ft/ncp/dao/SendgiftMapper.xml")
    employee2.appendChild(name3B3)

    #3B4
    name3B4=dom.createElement('mapper')
    name3B4.setAttribute("resource","com/ft/ncp/dao/SilencedUserInfoMapper.xml")
    employee2.appendChild(name3B4)

    #3B5
    name3B5=dom.createElement('mapper')
    name3B5.setAttribute("resource","com/ft/ncp/dao/PushMsgMapper.xml")
    employee2.appendChild(name3B5)

    #3B6
    name3B6=dom.createElement('mapper')
    name3B6.setAttribute("resource","com/ft/ncp/dao/PushMsgAndroidMapper.xml")
    employee2.appendChild(name3B6)

    #3B7
    name3B7=dom.createElement('mapper')
    name3B7.setAttribute("resource","com/ft/ncp/dao/GameNoticeInfoMapper.xml")
    employee2.appendChild(name3B7)

    #3B8
    name3B8=dom.createElement('mapper')
    name3B8.setAttribute("resource","com/ft/ncp/dao/OperationActivityMapper.xml")
    employee2.appendChild(name3B8)

    #3B9
    name3B9=dom.createElement('mapper')
    name3B9.setAttribute("resource","com/ft/ncp/dao/OperationPackageMapper.xml")
    employee2.appendChild(name3B9)

    #3B10
    name3B10=dom.createElement('mapper')
    name3B10.setAttribute("resource","com/ft/ncp/dao/OperationDailyGiftMapper.xml")
    employee2.appendChild(name3B10)

    #3B11
    name3B11=dom.createElement('mapper')
    name3B11.setAttribute("resource","com/ft/ncp/dao/PlayerInfoMapper.xml")
    employee2.appendChild(name3B11)

    # 3B12
    name3B12 = dom.createElement('mapper')
    name3B12.setAttribute("resource", "com/ft/ncp/dao/GiftCodeMapper.xml")
    employee2.appendChild(name3B12)

    # 3B13
    name3B13 = dom.createElement('mapper')
    name3B13.setAttribute("resource", "com/ft/ncp/dao/FrozenInfoMapper.xml")
    employee2.appendChild(name3B13)

    # 3B14
    name3B14 = dom.createElement('mapper')
    name3B14.setAttribute("resource", "com/ft/ncp/dao/ServerVersionInfoMapper.xml")
    employee2.appendChild(name3B14)

    # 3B15
    name3B15 = dom.createElement('mapper')
    name3B15.setAttribute("resource", "com/ft/ncp/dao/ServerReloadCsvInfoMapper.xml")
    employee2.appendChild(name3B15)

    # 3B16
    name3B16 = dom.createElement('mapper')
    name3B16.setAttribute("resource", "com/ft/ncp/dao/PlayerNameManagerMapper.xml")
    employee2.appendChild(name3B16)

    # 3B17
    name3B17 = dom.createElement('mapper')
    name3B17.setAttribute("resource", "com/ft/ncp/dao/UserBetaTestPurchaseMapper.xml")
    employee2.appendChild(name3B17)



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


    print "GMConfiguration.xml 创建"
