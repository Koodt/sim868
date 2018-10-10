#!/usr/bin/python

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('', 10000)
print >> sys.stderr, 'starting up on %s port %s' % serverAddress
sock.bind(serverAddress)

sock.listen(1)

while True:
    print >> sys.stderr, 'waiting for connection'
    try:
        connection, client_address = sock.accept()

        try:
            print >> sys.stderr, 'connection from', client_address

            while True:
                data = connection.recv(16)
                print >> sys.stderr, 'received "%s"' % data
                if data:
                    print >> sys.stderr, 'sending data back to the client'
                    connection.sendall(data)
                else:
                    print >> sys.stderr, 'no more dat from', client_address
                    break
        finally:
            connection.close()
    except (KeyboardInterrupt, SystemExit):
        print >> sys.stderr, 'Exit'
        sys.exit(0)
