class Kdefault(object):
    def __init__(self, path):
        self.path = path

    def removeDefaultDir(self):
        import os, shutil
        if os.path.exists(self.path):
            print("removing %s" % self.path)
            shutil.rmtree(self.path, ignore_errors=True)
        else:
            print("%s not exists" % self.path)

    def createDefaultDir(self):
        import os
        if not os.path.exists(self.path):
            print("creating %s" % self.path)
            os.makedirs(self.path)
        else:
            print("%s exists" % self.path)

    def generateDefaultJSON(self, defaultFile):
        self.defaultFile = self.path + defaultFile
        import json, os

        data = {
            "services": {
                "collector": {"collectorPort": 27072, "collectorHost": "k0dt.ru"},
                "harvester": {"AESkey": "f861feab561441c0e1fdcba91581dd95"},
            }
        }

        if not os.path.isfile(self.defaultFile):
            os.mknod(self.defaultFile)
        with open(self.defaultFile, 'w') as defaultJSON:
            json.dump(data, defaultJSON)

class KSocket(object):
    def __init__(self, dataJSON):
        self.dataJSON = dataJSON

    def setConnection(self):
        import socket
        import time
        import sys
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverAddress = ('', int(self.dataJSON["services"]["collector"]["collectorPort"]))
        print('starting up on %s port %s' % serverAddress)
        try:
            sock.bind(serverAddress)
            print('Started on %s port %s' % serverAddress)
        except socket.error as message:
            print >> sys.stderr, 'Socket error %s' % message
            sys.exit(0)

        sock.listen(1)

        while True:
            print('waiting for connection')
            try:
                connection, client_address = sock.accept()

                try:
                    print('connection from', client_address)

                    data = connection.recv(32)
                    decryptMessage = decryptData(data)
                    if '1111111111111111' in decryptMessage:
                        sys.exit(0)
                    print('received "%s"' % decryptMessage)
                finally:
                    connection.close()
            except SystemExit:
                print('System exit')
                sys.exit(0)
            except KeyboardInterrupt:
                print('From keyboard')
                sys.exit(0)

class Kjson(object):
    def __init__(self, pathJSON):
        self.pathJSON = pathJSON

    def getJSONdata(self):
        import json
        import sys

        try:
            fileJSON = open(self.pathJSON, 'r').read()
            data = json.loads(fileJSON)
            print(data["services"]["collector"]["collectorPort"])
            return data
        except IOError as errMessage:
            print('I/O error(%s): %s - %s' % (
                errMessage.errno,
                errMessage.filename,
                errMessage.strerror,
            ))
            sys.exit(0)

class Kcrypto(object):
    def __init__(self, path):
        self.path = path

    def createKeysPair(self):
        from Crypto.PublicKey import RSA
        from Crypto import Random
        from pathlib import Path
        import os

        prvFile = 'private.pem'
        pubFile = 'public.pem'
        randomGenerator = Random.new().read

        privateKey = RSA.generate(1024, randomGenerator)
        publicKey = privateKey.publickey()

        if not os.path.isfile(self.path + prvFile):
            with open(self.path + prvFile, 'w') as privateFile:
                print(privateFile, privateKey.exportKey())
        else:
            print('%s exists' % prvFile)

        if not os.path.isfile(self.path + pubFile):
            with open(self.path + pubFile, 'w') as publicFile:
                print(publicFile, publicKey.exportKey())
        else:
            print('%s exists' % pubFile)
