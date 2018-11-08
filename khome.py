#!/usr/bin/python3

import sys
import argparse
from kLibs import Kdefault, Binder, Kjson

parser = argparse.ArgumentParser(description='khome')
parser.add_argument('-r', '--role', action='store', dest='khomeRole', help='select role from collector and harvester')
parser.add_argument('-f', '--file', action='store', dest='filename', nargs='?', type=argparse.FileType('r'), help='Set full path to parsing file')
parser.add_argument('-k', '--key', action='store_true', help='create keys pair')
parser.add_argument('-d', '--default', action='store_true', help='create default configs and dir. ATTENTION!!! REMOVE OLD!!!')
results = parser.parse_args()

defaultConf = Kdefault('/opt/khome/defaults/')
getDataJSON = Kjson('/opt/khome/defaults/default.json').getJSONdata()

if results.default:
    defaultConf.removeDefaultDir()
    defaultConf.createDefaultDir()
    defaultConf.createKeysPair()
    defaultConf.generateDefaultJSON()

if results.key:
    defaultConf.createKeysPair()

if results.khomeRole == 'collector':
    getCollector = Binder(getDataJSON).setConnection()
    print('collector')
elif results.khomeRole == 'harvester':
    print('harvester')
else:
    print('What do you want, Jackson?')
    sys.exit()

#data = Kjson(results.filename)

#if bool(data["services"]["RSAgenerator"]["subscribe"]) == True:
#    print("True")
#    print(data["services"]["collector"]["collectorPort"])
