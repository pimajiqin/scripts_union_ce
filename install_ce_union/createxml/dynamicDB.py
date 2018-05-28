#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: 陈二狗

import xml.dom.minidom

from conf.config import *
from mkpath import *


def dynamicDB(channel, sid, DynamicPort):

    xmlpath = xml_path + '%s/%s/dynamicDB.xml' % (channel,sid)
    mkdir(xml_path + channel + sid)

    # 创建根
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'config', None)
    root = dom.documentElement

    # 21
    A21 = dom.createElement('port')
    A21T = dom.createTextNode(DynamicPort)
    root.appendChild(A21)
    A21.appendChild(A21T)

    # 22
    A22 = dom.createElement('name')
    A22T = dom.createTextNode('NoSQL')
    root.appendChild(A22)
    A22.appendChild(A22T)

    # 23
    A23 = dom.createElement('default')
    A23T = dom.createTextNode('data/default')
    root.appendChild(A23)
    A23.appendChild(A23T)

    # 24
    A24 = dom.createElement('services')
    root.appendChild(A24)

    # 31
    A31 = dom.createElement('service')
    A24.appendChild(A31)

    # 41
    A41 = dom.createElement('path')
    A41T = dom.createTextNode('data/user')
    A31.appendChild(A41)
    A41.appendChild(A41T)

    # 42
    A42 = dom.createElement('name')
    A42T = dom.createTextNode('user')
    A31.appendChild(A42)
    A42.appendChild(A42T)

    # 32
    A32 = dom.createElement('service')
    A24.appendChild(A32)

    # 43
    A43 = dom.createElement('path')
    A43T = dom.createTextNode('data/recipt')
    A32.appendChild(A43)
    A43.appendChild(A43T)

    # 44
    A44 = dom.createElement('name')
    A44T = dom.createTextNode('recipt')
    A32.appendChild(A44)
    A44.appendChild(A44T)

    # 25
    A25 = dom.createElement('backuphost')
    A25T = dom.createTextNode('127.0.0.1')
    root.appendChild(A25)
    A25.appendChild(A25T)

    # 26
    A26 = dom.createElement('backupport')
    A26T = dom.createTextNode('9001')
    root.appendChild(A26)
    A26.appendChild(A26T)


    f = open(xmlpath, 'w')
    dom.writexml(f, addindent='    ', newl='\n',  encoding = 'utf-8',)
    f.close()

    print "dynamicDB.xml 创建"
