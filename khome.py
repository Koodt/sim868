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
defaultData = {
          "services": {
            "kclient": {
              "AESkey": "f861feab561441c0e1fdcba91581dd95"
            },
            "kserver": {
              "serverHost": "127.0.0.1",
              "serverPort": 27072
            }
          }
        }

if len(sys.argv) < 2:
    parser.print_help()
    sys.exit()

if not os.path.isfile(defaultPath + defaultJSON) and not results.default:
    print('Config not exist')
    sys.exit()

if results.default:
    if defaultConf.checkDefaultConfig():
        defaultConf.removeDefaultDir()
    defaultConf.createDefaultDir()
    defaultConf.jsonCreator(defaultJSON, defaultData)
    Kcrypto(defaultPath).createKeysPair()
    sys.exit()

if results.key:
    Kcrypto(defaultPath).createKeysPair()

getDataJSON = Kjson(defaultPath + defaultJSON).getJSONdata()

if results.khomeRole == 'kserver':
    startKServer = KSocket(getDataJSON).startListener()
elif results.khomeRole == 'kclient':
    startKClient = KSocket(getDataJSON).setConnection()
else:
    print('[ ! ] Role not known')
    sys.exit()
