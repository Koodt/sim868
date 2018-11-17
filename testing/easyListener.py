#!/usr/bin/python3

import socket
import sys

serverAddress = ('', 27072)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(serverAddress)
sock.listen(1)

while True:
    print('[...] Waiting for connection')
    try:
        connection, client_address = sock.accept()
        try:
            print('[ + ] Connection from %s' % client_address)
        finally:
            connection.close()
    except SystemExit:
        print('[ ! ] System exit')
        sys.exit(0)
    except KeyboardInterrupt:
        print('[ ! ] From keyboard')
        sys.exit(0)
