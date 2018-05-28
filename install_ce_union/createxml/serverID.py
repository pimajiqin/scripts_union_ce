#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: 陈二狗

import xml.dom.minidom

from conf.config import *
from mkpath import *


def serverID(channel, sid):

    xmlpath = xml_path + '%s/%s/serverID.xml' % (channel,sid)
    mkdir(xml_path + channel + sid)

    # 创建根
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'Config', None)
    root = dom.documentElement

    # 21
    A21 = dom.createElement('defaultID')
    A21T = dom.createTextNode(sid)
    root.appendChild(A21)
    A21.appendChild(A21T)


    f = open(xmlpath, 'w')
    dom.writexml(f, addindent='    ', newl='\n',  encoding = 'utf-8',)
    f.close()

    print "serverID.xml 创建"

