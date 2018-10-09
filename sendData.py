#!/usr/bin/python

import serial
import time

phone = serial.Serial("/dev/ttyS0", 115200)

def writeQuery(query):
    phone.write(query)

for command in ["AT+CIPSEND\r\n", "VerySecretData\r\n\x1A"]:
    writeQuery(command)
    time.sleep(1)
