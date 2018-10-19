#!/usr/bin/python

import json
import sys

def getPortFromJSON():
    with open('default.json') as sourceJSON:
        data = json.load(sourceJSON)
        return data['targetPort'], data['targetHost']

targetPort, targetHost = getPortFromJSON()

print >> sys.stderr, '%s:%s' % (targetHost, targetPort)

fileJSON = open('default.json').read()

data = json.loads(fileJSON)
print(data['targetPort'])
