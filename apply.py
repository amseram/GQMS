#!/usr/bin/env python2
#coding=utf8
"""
# Author: amsera
# Created Time : 2018-05-29 14:03:14

# File Name: apply.py
# Description:
# Apply an account on GQMS (console version)
"""

import sys,socket


class create_connect:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def initial(self,add,port=80):
        self.conn   = self.socket.connect((add,port))
    def send(self,query):
        self.mess   = query
        self.sent   = self.socket.sendall(self.mess.encode('ascii'))
        self.data   = self.socket.recv(64).decode('utf8')

class show_option:
    def __init__(self):
        self.sock = create_connect()
        self.sock.initial("gqms.shu.edu.cn",8080)
        self.options = {}
        self.options['0'] = "GQMS application options:\n"
        self.options['1'] = "[1]     Apply an account \n"
        self.options['2'] = "[2]     Check acc querys \n"
        self.options['3'] = "[3]     Set ur passwords\n"
        self.options['4'] = "[4]     Exit"
        for i in range(5):
            print self.options.get(str(i)).strip()
        while True:
            while True:
                try :
                    targ = int(raw_input("Select : "))
                    break
                except ValueError:
                    print "Plz input an integer"
            self.select(targ)
    def select(self,targ=0):
        self.targ = targ
        if targ == 0 :
            for i in range(5):
                print self.options.get(str(i)).strip()
        if targ == 4 :
            sys.exit(0)
        if targ == 1 :
            mailaddr = ""
            username = ""
            supervisor = ""
            while mailaddr == "" or username == "" or supervisor == "":
                username = str(raw_input("username : "))
                mailaddr = str(raw_input("mailaddr : "))
                supervisor = str(raw_input("supervisor : "))
            self.sock.send("gqms,apply,"+str(supervisor)+","+str(username)+","+str(mailaddr))
            print self.sock.data
        if targ == 2 :
            username = ""
            while username == "":
                username = str(raw_input("username : "))
            self.sock.send("gqms,check,"+str(username))
            print self.sock.data
        if targ == 3 :
            username = ""
            passwd   = ""
            curpass  = ""
            while passwd == "" or username == "" or curpass == "":
                username = str(raw_input("username : "))
                curpass  = str(raw_input("current passwd : "))
                passwd   = str(raw_input("neopasswd : "))
                tmppss   = str(raw_input("retype passwd : "))
                if tmppss != passwd :
                    passwd = ""
            self.sock.send("gqms,passwd,"+str(curpass)+","+str(passwd)+","+str(username))
            print self.sock.data

if __name__ == "__main__":
    print "#"*50
    print " "*12+"GQMS application system bate 01"
    print "#"*50
    test = show_option()
