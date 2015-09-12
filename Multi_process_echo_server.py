#!/usr/bin/env python

# A simple Python script for Multi-processes ECHO server

# import required modules

import socket
from  multiprocessing import Process
import sys

# Function defination. This function will be called from Process created

def EchoClientHandler(clientSocket, addr) :
        while 1:
                client_data = clientSocket.recv(2048)
                print " [*] Client says: %s" % client_data

                if client_data:

                        clientSocket.send(client_data)
                        print  " [*] I said:  %s" % client_data
                else:
                        clientSocket.close()
                        return

# Create a TCP socket

print " [*] Creating a TCP socket..."

tcpSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM  )

# Connection crashed? Reuse the socket immediately

tcpSocket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

# Bind TCP socket to a port

print " [*] Trying to bind to given port..."
tcpSocket.bind(( "0.0.0.0", int(sys.argv[1])  )  )

# Listen on this port now

tcpSocket.listen(10)
print " [*] Listening on given port..."

# Start a worker process , an empty list


workerProcesses = []
print " [*] Worker process started..."
# Put the server in accept mode, ready for client connections

while 1:
        print " [*] Ready for client connections.."

        # Start a new process
        print " Starting a new thread/process to service client.."
        cSock, addr = tcpSocket.accept()
        worker = Process(target=EchoClientHandler, args= (cSock, addr))

        # start the process.
        worker.start()
        workerProcesses.append(worker)

# Commented code

        """ if __name__ = '__main__':
                q = Queue()
                p = Process(target=f, args=(q, (cSock,addr)) )
                p.start()
                #print q.get()
                p.join """
