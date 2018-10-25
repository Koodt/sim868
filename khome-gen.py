#!/usr/bin/python
import sys
import json
from Crypto.PublicKey import RSA
from Crypto import Random

def createKeysPair():
    randomGenerator = Random.new().read
    privateKey = RSA.generate(1024, randomGenerator)
    publicKey = privateKey.publickey()
    with open("private.pem", "w") as privateFile:
        print >> privateFile, privateKey.exportKey()

    with open("public.pem", "w") as publicFile:
        print >> publicFile, publicKey.exportKey()
