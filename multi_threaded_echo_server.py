#!/usr/bin/env python

# A simple python script for multi threaded Echo Server using Socket programming

# Import module socket and thread

import socket
import thread
import sys

# Define a function that will be called from thread. This function will receive data from client and echo the same data back to the client

def EchoClientHandler(clientSocket,addr) :
        while 1:
                # Recieve data from client-socket

                client_data = clientSocket.recv(2048)
                print " [*] Client says: %s " % client_data

                if client_data:
                        # Send data back to client if recieved earlier
                        clientSocket.send(client_data)
                        print " I said: %s " % client_data
                else:
                        clientSocket.close()
                        return


# Create a TCP socket

print " [*] Creating a TCP Socket.."
tcpSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM  )

# Connected aborted or crashed? Reuse the socket immediately

tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Now bind this TCP socket to a port. Get command line parameter 'sys.argv[1]' from user

print " [*] Trying to bind the socket to  given port %d "

tcpSocket.bind( (  "0.0.0.0" , int(sys.argv[1])  )  )

# Start listening for 10 connections max on this port now

print " [*] Listening for incoming connections on port %d on all interfaces"
tcpSocket.listen(10)

# Put the server in accept mode to create a client-socket object. In while loop

while 1:
        print  " [*] Ready to acccept client connections.."
        cSock,addr =    tcpSocket.accept()

        # Start a new thread to service
        print "[*] Starting new thread.."
        thread.start_new_thread( EchoClientHandler, (cSock, addr) )

