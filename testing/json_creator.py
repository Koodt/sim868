import json
import os
import uuid

fileName = '/tmp/' + str(uuid.uuid4())

data = {
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

if not os.path.isfile(fileName):
    os.mknod(fileName)
with open(fileName, 'w') as defaultJSON:
    json.dump(data, defaultJSON)
