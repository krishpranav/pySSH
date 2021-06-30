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