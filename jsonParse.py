#!/usr/bin/python

import json

fileJSON = open('default.json').read()

data = json.loads(fileJSON)
print data
