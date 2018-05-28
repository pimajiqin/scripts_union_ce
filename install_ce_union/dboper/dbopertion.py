#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: 陈二狗

import MySQLdb
import MySQLdb.cursors


def select_logic_info(config, sid):
    """ 查找所有serverid和对应的ip """
    db = MySQLdb.connect(config["ip"], config["user"], config["passwd"], config["dbname"], cursorclass = MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute("SELECT * from drlogic WHERE ServerId = %s;" % sid)
    data = cursor.fetchone()
    return data
    db.close()

def select_arena_rank_info(ip, user, passwd, dbname):
    """ 查找新服插入数据是否正确 """
    db = MySQLdb.connect(ip, user, passwd, dbname, cursorclass = MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute("select count(*) from arena_rank_info;")
    data = cursor.fetchone()
    return data
    db.close()

def select_serverid_ip(config):
    """ 查找所有serverid和对应的ip """
    db = MySQLdb.connect(config["ip"], config["user"], config["passwd"], config["dbname"], cursorclass = MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute("SELECT Ip,ServerId,NatPort from drlogic;")
    data = cursor.fetchall()
    return data
    db.close()

