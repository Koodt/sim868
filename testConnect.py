#!/usr/bin/python
import json
import socket
import sys
from Crypto.Cipher import AES
from Crypto import Random

key = b'f861feab561441c0e1fdcba91581dd95'
iv = Random.new().read(AES.block_size)
obj = AES.new(key, AES.MODE_CBC, iv)

def getDataFromJSON():
    with open('default.json') as sourceFile:
        data = json.load(sourceFile)
        return data['targetHost'], int(data['targetPort'])

def encryptData(message):
    encryptText = iv + obj.encrypt(message)
    return encryptText

def decryptData(message):
    decryptText = obj.decrypt(message)
    return decryptText

def get_constants(prefix):
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix)
                 )

targetHost, targetPort = getDataFromJSON()

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# Create a TCP/IP socket
sock = socket.create_connection((targetHost, targetPort))

print >> sys.stderr, 'Family  :', families[sock.family]
print >> sys.stderr, 'Type    :', types[sock.type]
print >> sys.stderr, 'Protocol:', protocols[sock.proto]
print >> sys.stderr

try:

    # Send data
    #message = raw_input()
    message = b'1111111111111111'
    encryptMessage = encryptData(message)
    print >> sys.stderr, 'sending "%s"' % encryptMessage
    sock.sendall(encryptMessage)
    decryptMessage = decryptData(encryptMessage)
    print >> sys.stderr, 'local decrypting "%s"' % decryptMessage

finally:
    print >> sys.stderr, 'closing socket'
    sock.close()
