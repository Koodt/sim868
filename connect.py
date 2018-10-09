#!/usr/bin/python

import serial
import time

phone = serial.Serial("/dev/ttyS0", 115200)

def writeQuery(query):
    phone.write(query)

for command in ["AT+CGATT=1\r\n",
              "AT+CSTT\r\n",
              "AT+CIICR\r\n",
              "AT+CIFSR\r\n",
              "AT+CIPSTART=\"TCP\", \"target.host\", \"5003\"\r\n"]:
    writeQuery(command)
    time.sleep(1)
