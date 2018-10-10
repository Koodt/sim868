#!/usr/bin/python

import socket

sock = socket.socket()

sock.bind( ('', 5003) )
sock.listen(5)
conn, addr = sock.accept()
conn.settimeout(10)
data = conn.recv(1024)

if not data:
    print('No data')
    conn.close()

udata = data.decode('utf-8')
print('Data: ' + udata)

conn.close()
