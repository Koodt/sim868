#!/usr/bin/python

import socket
import sys
import json
import argparse
from Crypto.Cipher import AES
from Crypto import Random

def getDataFromJSON(filename):
    try:
        with filename as sourceFile:
            data = json.load(sourceFile)
            sourceFile.close()
            return data
    except IOError as errMessage:
        print >>sys.stderr, "I/O error(%s): %s - %s" % (
            errMessage.errno,
            errMessage.filename,
            errMessage.strerror,
        )
        sys.exit(0)

def bindSocket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverAddress = ('', int(getDataFromJSON()["targetPort"]))
    print 'starting up on %s port %s' % serverAddress
    try:
        sock.bind(serverAddress)
    except socket.error as message:
        print >> sys.stderr, 'Socket error %s' % message
        sys.exit(0)

parser = argparse.ArgumentParser(description='khome')
parser.add_argument('-r', '--role', action='store', dest='khomeRole', help='select role from collector and harvester')
parser.add_argument('-f', '--file', action='store', dest='filename', nargs='?', type=argparse.FileType('r'), help='Set full path to parsing file')
results = parser.parse_args()

if results.khomeRole != 'collector' and results.khomeRole != 'harvester':
    print 'Go away upizdok'
    sys.exit()

if results.khomeRole == 'collector':
    print('collector')
elif results.khomeRole == 'harvester':
    print('harvester')

if bool(getDataFromJSON(results.filename)["services"]["RSAgenerator"]["subscribe"]) == True:
    print "True"
    print getDataFromJSON(results.filename)["services"]["collector"]["collectorPort"]
