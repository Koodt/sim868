#!/usr/bin/python
import json
import socket
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto import Random


def getDataFromJSON():
    try:
        with open("default.json") as sourceFile:
            data = json.load(sourceFile)
            return (
                data["targetHost"],
                int(data["targetPort"]),
                bytes(data["messages"][0]),
                bytes(data["AESkey"]),
                str(data["RSAkeys"]["privateFile"]),
                str(data["RSAkeys"]["publicFile"]),
            )
    except IOError as errMessage:
        print >>sys.stderr, "I/O error(%s): %s - %s" % (
            errMessage.errno,
            errMessage.filename,
            errMessage.strerror,
        )
        sys.exit(0)


targetHost, targetPort, message, key, privateFile, publicFile = getDataFromJSON()
iv = Random.new().read(AES.block_size)
obj = AES.new(key, AES.MODE_CBC, iv)


def getRSAKeys(privateFile, publicFile):
    with open(privateFile, "r") as sourceFile:
        privateKeyStr = sourceFile.read()
    sourceFile.close()
    with open(publicFile, "r") as sourceFile:
        publicKeyStr = sourceFile.read()
    sourceFile.close()
    privateKey = RSA.importKey(privateKeyStr)
    publicKey = RSA.importKey(publicKeyStr)
    return (privateKey, publicKey)


def encryptData(message):
    encryptText = iv + obj.encrypt(message)
    return encryptText


def decryptData(message):
    decryptText = obj.decrypt(message)
    return decryptText


def get_constants(prefix):
    return dict((getattr(socket, n), n) for n in dir(socket) if n.startswith(prefix))


families = get_constants("AF_")
types = get_constants("SOCK_")
protocols = get_constants("IPPROTO_")

try:
    sock = socket.create_connection((targetHost, targetPort))
except socket.error as errMessage:
    print >>sys.stderr, "Socket error(%s): %s" % (errMessage.errno, errMessage.strerror)
    sys.exit(0)

print >>sys.stderr, "Family   :", families[sock.family]
print >>sys.stderr, "Type     :", types[sock.type]
print >>sys.stderr, "Protocol :", protocols[sock.proto]
print >>sys.stderr

try:
    encryptMessage = encryptData(message)
    print >>sys.stderr, 'sending "%s"' % encryptMessage
    sock.sendall(encryptMessage)
    decryptMessage = decryptData(encryptMessage)
    print >>sys.stderr, 'local decrypting "%s"' % decryptMessage

finally:
    print >>sys.stderr, "closing socket"
    sock.close()
