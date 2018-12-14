#!/usr/bin/python3

import sys
import argparse
import os
from kLibs import Kdefault, KSocket, Kjson, Kcrypto

parser = argparse.ArgumentParser(description='khome')
parser.add_argument('-r', '--role', action='store', dest='khomeRole', help='select role from collector and harvester')
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
    defaultConf.removeDefaultDir()
    defaultConf.createDefaultDir()
    defaultConf.generateDefaultJSON(defaultJSON)
    Kcrypto(defaultPath).createKeysPair()

if results.key:
    Kcrypto(defaultPath).createKeysPair()

getDataJSON = Kjson(defaultPath + defaultJSON).getJSONdata()

if results.khomeRole == 'collector':
    startCollector = KSocket(getDataJSON).startListener()
elif results.khomeRole == 'harvester':
    startHarvester = KSocket(getDataJSON).setConnection()
else:
    print('[ ! ] Role not known')
    sys.exit()    

#data = Kjson(results.filename)

#if bool(data["services"]["RSAgenerator"]["subscribe"]) == True:
#    print("True")
#    print(data["services"]["collector"]["collectorPort"])
