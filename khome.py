#!/usr/bin/python3

import sys
import argparse
import os
from kLibs import Kdefault, KSocket, Kjson, Kcrypto, MongoStatic

parser = argparse.ArgumentParser(description='khome')
parser.add_argument('-r', '--role', action='store', dest='khomeRole', help='select role. example --role kserver | kclient')
parser.add_argument('-f', '--file', action='store', dest='filename', nargs='?', type=argparse.FileType('r'), help='Set full path to parsing file')
parser.add_argument('-k', '--key', action='store_true', help='create keys pair')
parser.add_argument('-d', '--default', action='store_true', help='create default configs and dir. ATTENTION!!! REMOVE OLD!!!')
results = parser.parse_args()

defaultPath = '/opt/khome/defaults/'
defaultJSON = 'default.json'
defaultConf = Kdefault(defaultPath)

if len(sys.argv) < 2:
    parser.print_help()
    sys.exit()

if not os.path.isfile(defaultPath + defaultJSON) and not results.default:
    print('Config not exist')
    sys.exit()

if results.default:
    print('[!!!] Warning. Remove old configs. Are you sure? For attempt print capital yes')
    answer = input()
    if answer == 'YES':
        defaultConf.removeDefaultDir()
        defaultConf.createDefaultDir()
        defaultConf.generateDefaultJSON(defaultJSON)
        Kcrypto(defaultPath).createKeysPair()
    else:
        print('[ - ] Cancelled')
    sys.exit()

if results.key:
    Kcrypto(defaultPath).createKeysPair()

getDataJSON = Kjson(defaultPath + defaultJSON).getJSONdata()

if results.khomeRole == 'kserver':
    startKServer = KSocket(getDataJSON).startListener()
elif results.khomeRole == 'kciient':
    startKClient = KSocket(getDataJSON).setConnection()
else:
    print('[ ! ] Role not known')
    sys.exit()
