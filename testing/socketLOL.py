#!/usr/bin/python

import socket

#def retBanner(ip, port):
#    try:
#        socket.setdefaulttimeout(2)
#        sock = socket.socket()
#        sock.connect((ip, port))
#    except:

socket.setdefaulttimeout(2)

sock = socket.socket()

try:
    sock.connect(('192.168.56.101', 27072))
except:
    print("ERROR")
            
