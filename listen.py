#!/usr/bin/python

import socket
import sys
from Crypto.Cipher import AES
from Crypto import Random

key = b'f861feab561441c0e1fdcba91581dd95'
iv = Random.new().read(AES.block_size)
obj = AES.new(key, AES.MODE_CBC, iv)

def decryptData(message):
    decryptText = obj.decrypt(message)
    return decryptText

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('', 10000)
print >> sys.stderr, 'starting up on %s port %s' % serverAddress

try:
    sock.bind(serverAddress)
except socket.error as message:
    print >> sys.stderr, 'Socket error %s' % message
    sys.exit(0)

sock.listen(1)

while True:
    print >> sys.stderr, 'waiting for connection'
    try:
        connection, client_address = sock.accept()

        try:
            print >> sys.stderr, 'connection from', client_address

            while True:
                data = connection.recv(32)
                decryptMessage = decryptData(data)
                print >> sys.stderr, 'received "%s"' % decryptMessage
        finally:
            connection.close()
    except SystemExit:
        print >> sys.stderr, 'System exit'
        sys.exit(0)
    except KeyboardInterrupt:
        print >> sys.stderr, 'From keyboard'
        sys.exit(0)
