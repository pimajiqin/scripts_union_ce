#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: 陈二狗

import paramiko

class SCP_SSH(object):

    def __init__(self,ip,):
        self.ip = ip

    def __gpath__(self,gpath):
        self.gpath = gpath

    def ssh(self,command):
        private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
        transport = paramiko.Transport((self.ip, 22))
        transport.connect(username='root', pkey=private_key)
        ssh = paramiko.SSHClient()
        ssh._transport = transport
        stdin, stdout, stderr = ssh.exec_command(command)
        result = stdout.read()
        transport.close()
        return result

    def scp(self,localpath,remotepath):
        private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
        trans = paramiko.Transport((self.ip, 22))
        trans.connect(username='root', pkey=private_key)
        sftp = paramiko.SFTPClient.from_transport(trans)
        sftp.put(localpath=localpath, remotepath=remotepath)
        trans.close()