import serial
import time
import os
from datetime import datetime

if 'PHONENUMBER' in os.environ:
    phoneNumber = os.environ['PHONENUMBER']
else:
    phoneNumber = input('Phone number (format +XXXXXXXXXXX): ')

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime('%d-%b-%Y %H:%M:%S')
messageStr = 'Some text'
phone = serial.Serial('/dev/ttyS0', 115200)

phone.write(b'AT+CMGF=1\r')
phone.write(b'AT+CSCS="GSM"\r')
phone.write(('AT+CMGS="%s"\r' % phoneNumber).encode('ascii'))
time.sleep(2)
phone.write(('Timestamp: %s\n\nMessage: %s' % (timestampStr, messageStr)).encode('ascii'))
phone.write(b'\x1A')
phone.close()
