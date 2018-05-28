#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: 陈二狗



from ActivityBossConfiguration import *
from Configuration import *
from dynamicDB import *
from GMConfiguration import *
from serverID import *
from server import *
from WarConfiguration import *
from install_ce_union.dboper.dbopertion import *




def creat_all_xml(channel, config, sid):

    serverinfo = select_logic_info(config, sid)

    sid = serverinfo['ServerId']
    ActivityBossIp = serverinfo['ActivityBossIp']
    ActivityBossDbName = serverinfo['ActivityBossDbName']
    ActivityBossDbUser = serverinfo['ActivityBossDbUser']
    ActivityBossDbPw = serverinfo['ActivityBossDbPw']
    DbIp = serverinfo['DbIp']
    DbName = serverinfo['DbName']
    DbPw = serverinfo['DbPw']
    DbUser = serverinfo['DbUser']
    DynamicPort = serverinfo['DynamicPort']
    AccountIP = serverinfo['AccountIP']
    AccountDbName = serverinfo['AccountDbName']
    AccountDbUser = serverinfo['AccountDbUser']
    AccountDbPw = serverinfo['AccountDbPw']
    GamePort = serverinfo['GamePort']
    CsIp = serverinfo['CsIp']
    CsPort = serverinfo['CsPort']
    AsIp = serverinfo['AsIp']
    AsPort = serverinfo['AsPort']
    CsDbName = serverinfo['CsDbName']
    CsDbUser = serverinfo['CsDbUser']
    CsDbPw = serverinfo['CsDbPw']

    ActivityBossConfiguration(channel, sid, ActivityBossIp, ActivityBossDbName, ActivityBossDbUser, ActivityBossDbPw)
    Configuration(channel, sid, DbIp, DbName, DbUser, DbPw)
    dynamicDB(channel, sid, DynamicPort)
    GMConfiguration(channel, sid, AccountIP, AccountDbName, AccountDbUser, AccountDbPw)
    serverID(channel, sid)
    server(channel, sid, GamePort, CsIp, CsPort, AsIp, AsPort)
    WarConfiguration(channel, sid, CsIp, CsDbName, CsDbUser, CsDbPw)


