#!/usr/bin/env python3 

# imports
import sys
import socket
import argparse
import logging 

import paramiko


class SSH_Server(paramiko.ServerInterface):
    def check_auth_password(self, user, passwd):
        print "[*] Connection Attempt: user=> " + str(user) + " | passwd=> " + str(passwd)
        return paramiko.AUTH_FAILED

def Reveal(keyfile, port):
    print "\n==================== pySSH (SSH Password Revieler) ===================="
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', port))
        s.listen(5)
        while 1:
            client, addr = s.accept()
            sess = paramiko.Transport(client)
            sess.add_server_key(paramiko.RSAKey(filename=keyfile))
            sess.start_server(server=SSH_Server())
    except Exception as e:
        print "[-] Exception: " + str(e)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('-k', '--keyfile')
    p.add_argument('-p', '--port', type=int)
    args = p.parse_args()
    
    