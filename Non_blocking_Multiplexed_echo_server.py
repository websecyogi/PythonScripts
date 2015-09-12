#!/usr/bin/env python

# A simple non blocking multiplexed ECHO server using select()

"""  Author: WebSecYogi
https://github.com/websecyogi/PythonScripts

"""

# Import modules: socket , select

import socket,select

print " [*] Creating a TCP socket connection..."

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Reuse the connection immediately after it is terminated/aborted

tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

# Set port number

port = 8888

print " [*] Trying to bind the TCP socket to all interfaces on port %d ... " % port

tcpSocket.bind(("0.0.0.0", port))

print " [*] Entering listening mode..."

tcpSocket.listen(10)

print " [*] Waiting for connection on port :", port

# An empty list, a  socket

holeinsock = []

while True:
        # Multiplexing technique: Wait to read/write data into following sockets. If there is data to read or socket is ready write, wake me up.
        # Call select() and parse it a list of sockets.
        
         read,write, ex = select.select( [tcpSocket] + holeinsock, [] , []  )
        for s in read:
                if s is tcpSocket:
                        (client , (ip, port)) = tcpSocket.accept()
                        print " [*] Incoming connection from IP %s on %s " %( ip, port )

                        print " [*] Starting ECHO output.."
                        holeinsock.append(client)

                else:
                        data = s.recv(2048)
                        if data == "":
                                holeinsock.remove(s)
                                print " [*] Closing connection with IP %s..." % ip

                        else:

                                print " [*] From IP %s on port %s : %s "  % (ip, port, data)

                                # Echo ( or send ) data back to client.
                                client.send( " [*] You sent:  " +  data)

