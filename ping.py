#!/usr/bin/python

import serial
import time

phone = serial.Serial("/dev/ttyS0", 115200)

def writeQuery(query):
    phone.write(query)

for command in ["AT+CIPPING=\"8.8.8.8\"\r\n"]:
    writeQuery(command)
    time.sleep(1)
