def createKeysPair(path):
    from Crypto.PublicKey import RSA
    from Crypto import Random
    randomGenerator = Random.new().read
    privateKey = RSA.generate(1024, randomGenerator)
    publicKey = privateKey.publickey()
    with open(path + 'private.pem', 'w') as privateFile:
        print >> privateFile, privateKey.exportKey()

    with open(path + 'public.pem', 'w') as publicFile:
        print >> publicFile, publicKey.exportKey()

def defaultDir(path):
    import os
    if not os.path.exists(path):
        print('creating %s' % path)
        os.makedirs(path)
    else:
        print('%s exists' % path)
