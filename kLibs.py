class Kdefault(object):
    def __init__(self, path):
        self.path = path

    def createKeysPair(self):
        from Crypto.PublicKey import RSA
        from Crypto import Random
        randomGenerator = Random.new().read
        privateKey = RSA.generate(1024, randomGenerator)
        publicKey = privateKey.publickey()
        with open(self.path + 'private.pem', 'w') as privateFile:
            print >> privateFile, privateKey.exportKey()

        with open(self.path + 'public.pem', 'w') as publicFile:
            print >> publicFile, publicKey.exportKey()

    def removeDefaultDir(self):
        import os, shutil
        if os.path.exists(self.path):
            print('removing %s' % self.path)
            shutil.rmtree(self.path, ignore_errors=True)
        else:
            print('%s not exists' % self.path)

    def createDefaultDir(self):
        import os
        if not os.path.exists(self.path):
            print('creating %s' % self.path)
            os.makedirs(self.path)
        else:
            print('%s exists' % self.path)

    def generateDefaultJSON(self):
        import json
        data = {"services":{"collector":{"collectorPort":27072,"collectorHost":"k0dt.ru"},"harvester":{"AESkey":"f861feab561441c0e1fdcba91581dd95"}}}
        with open(self.path + 'default.json', 'w') as defaultJSON:
            print >> defaultJSON, json.dumps(data)
