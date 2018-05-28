#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: 陈二狗

import xml.dom.minidom

from conf.config import *
from mkpath import *


def server(channel, sid, GamePort, CsIp, CsPort, AsIp, AsPort):


    xmlpath = xml_path + '%s/%s/server.xml' % (channel,sid)

    mkdir(xml_path + channel + sid)

    # 创建根
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'Config', None)
    root = dom.documentElement

    # 21
    A21 = dom.createElement('ip')
    A21T = dom.createTextNode('0.0.0.0')
    root.appendChild(A21)
    A21.appendChild(A21T)

    # 22
    A22 = dom.createElement('port')
    A22T = dom.createTextNode(GamePort)
    root.appendChild(A22)
    A22.appendChild(A22T)

    # 23
    A23 = dom.createElement('log')
    A23T = dom.createTextNode('cfg/logback.xml')
    root.appendChild(A23)
    A23.appendChild(A23T)

    # 24
    A24 = dom.createElement('protocol')
    A24T = dom.createTextNode('com.feelingtouch.dr.protocol')
    root.appendChild(A24)
    A24.appendChild(A24T)

    # 25
    A25 = dom.createElement('service')
    A25T = dom.createTextNode('com.ft.svc.pool')
    root.appendChild(A25)
    A25.appendChild(A25T)

    # 26
    A26 = dom.createElement('luadll')
    A26T = dom.createTextNode('./libs/libluajit-5.1.so')
    root.appendChild(A26)
    A26.appendChild(A26T)

    # 27
    A27 = dom.createElement('library')
    A27T = dom.createTextNode('./libs')
    root.appendChild(A27)
    A27.appendChild(A27T)


    # 28
    A28 = dom.createElement('translateid')
    A28T = dom.createTextNode('20170104000035193')
    root.appendChild(A28)
    A28.appendChild(A28T)

    # 29
    A29 = dom.createElement('translatekey')
    A29T = dom.createTextNode('mmjXQs1bff2JGz120dY8')
    root.appendChild(A29)
    A29.appendChild(A29T)

    # 210
    A210 = dom.createElement('microsoftKey')
    A210T = dom.createTextNode('09e7110dfa944cf780901187ab8c0848')
    root.appendChild(A210)
    A210.appendChild(A210T)

    # 211
    A211 = dom.createElement('savedb')
    A211T = dom.createTextNode('1')
    root.appendChild(A211)
    A211.appendChild(A211T)

    # 212
    A212 = dom.createElement('csip')
    A212T = dom.createTextNode(CsIp)
    root.appendChild(A212)
    A212.appendChild(A212T)

    # 213
    A213 = dom.createElement('csport')
    A213T = dom.createTextNode(CsPort)
    root.appendChild(A213)
    A213.appendChild(A213T)

    # 214
    A214 = dom.createElement('cs')
    A214T = dom.createTextNode('1')
    root.appendChild(A214)
    A214.appendChild(A214T)

    # 215
    A215 = dom.createElement('asip')
    A215T = dom.createTextNode(AsIp)
    root.appendChild(A215)
    A215.appendChild(A215T)

    # 216
    A216 = dom.createElement('asport')
    A216T = dom.createTextNode(AsPort)
    root.appendChild(A216)
    A216.appendChild(A216T)


    f = open(xmlpath, 'w')
    dom.writexml(f, addindent='    ', newl='\n',  encoding = 'utf-8',)
    f.close()

    print "server.xml 创建"

