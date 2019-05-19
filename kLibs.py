class Kdefault(object):
    def __init__(self, path):
        self.path = path

    def removeDefaultDir(self):
        import os, shutil
        if os.path.exists(self.path):
            print("[---] Removing %s" % self.path)
            shutil.rmtree(self.path, ignore_errors=True)
        else:
            print("[ - ] %s not exists" % self.path)

    def createDefaultDir(self):
        import os, sys
        if not os.path.exists(self.path):
            try:
                print("[+++] creating %s" % self.path)
                os.makedirs(self.path)
            except IOError as errMessage:
                print('[!!!] Error(%s): %s - %s' % (
                    errMessage.errno,
                    errMessage.filename,
                    errMessage.strerror,
                ))
                sys.exit(0)
        else:
            print("[+!+] %s exists" % self.path)

    def generateDefaultJSON(self, defaultFile):
        self.defaultFile = self.path + defaultFile
        import json, os

        data = {
            "services": {
                "kserver": {"serverPort": 27072, "serverHost": "127.0.0.1"},
                "kclient": {"AESkey": "f861feab561441c0e1fdcba91581dd95"},
            }
        }

        if not os.path.isfile(self.defaultFile):
            os.mknod(self.defaultFile)
        with open(self.defaultFile, 'w') as defaultJSON:
            json.dump(data, defaultJSON)

class KSocket(object):
    def __init__(self, dataJSON):
        self.dataJSON = dataJSON

    def startListener(self):
        import socket
        import time
        import sys

        def decryptData(message):
            decryptText = obj.decrypt(message)
            return decryptText

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverAddress = ('', int(self.dataJSON["services"]["kserver"]["serverPort"]))
        print('[...] Starting up on %s port %s' % serverAddress)
        try:
            sock.bind(serverAddress)
            print('[ + ] Started on %s port %s' % serverAddress)
        except socket.error as message:
            print('Socket error %s' % message)
            sys.exit(0)

        sock.listen(1)

        while True:
            print('[...] Waiting for connection')
            try:
                connection, client_address = sock.accept()

                try:
                    print('[ + ] Connection from', client_address)
                finally:
                    connection.close()
            except SystemExit:
                print('[ ! ] System exit')
                sys.exit(0)
            except KeyboardInterrupt:
                print('[ ! ] From keyboard')
                sys.exit(0)

    def setConnection(self):
        import socket
        import sys
        try:
            sock = socket.create_connection((self.dataJSON["services"]["kserver"]["serverHost"], self.dataJSON["services"]["kserver"]["serverPort"]))
        except socket.error as errMessage:
            print('[!!!] Socket error(%s): %s' % (
                errMessage.errno,
                errMessage.strerror
                ))
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
            ### example
            #print(data["services"]["kserver"]["serverPort"])
            return data
        except IOError as errMessage:
            print('[!!!] Error(%s): %s - %s' % (
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

        def checkAndCreateKey(createPath, createFile, createKey):
            def creatingKey(createPath, createFile, createKey):
                with open(createPath + createFile, 'w') as keyFile:
                    print(createKey.exportKey(format = 'PEM', pkcs = 1), file = keyFile)
            if os.path.isfile(createPath + createFile):
                answer = input('[ ! ] Key exist. Rewrite key? [y/N]: ')
                if answer.lower() == 'y' or answer.lower() == 'yes':
                    creatingKey(createPath, createFile, createKey)
                else:
                    print('[ ! ]Creating file was canceled by user')
            else:
                creatingKey(createPath, createFile, createKey)


        prvFile = 'private.pem'
        pubFile = 'public.pem'
        randomGenerator = Random.new().read

        privateKey = RSA.generate(1024, randomGenerator)
        publicKey = privateKey.publickey()

        checkAndCreateKey(self.path, prvFile, privateKey)
        checkAndCreateKey(self.path, pubFile, publicKey)

    def getCrypto(self):
        data = connection.recv(32)
        decryptMessage = decryptData(data)
        if '1111111111111111' in decryptMessage:
            sys.exit(0)
        print('[ + ] Received "%s"' % decryptMessage)

class MongoStatic:
    def __init__(self, inBase, inHost):
        import pymongo
        self.dBase = inBase
        self.dHost = inHost
        self.client = pymongo.MongoClient(self.dHost)

    def baseList(self):
        return self.client.list_database_names()

    def collList(self):
        return self.client.self.dBase.list_collection_names()

    def baseCheck(self):
        if self.dBase in self.baseList():
            return False
        else:
            return True

    def collCheck(self):
        if self.inColl in self.baseCheck():
            return False
        else:
            return True

    def baseCreate(self):
        self.myDb = self.client[self.dBase]

    def collectionCreate(self, inColl):
        self.posts = self.dBase[inColl]

    def toCollection(self, postData):
        self.postData = postData
        result = self.posts.insert_one(postData)

    def collectionFindAll():
        return
