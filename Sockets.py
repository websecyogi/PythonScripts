#!/usr/bin/env python

# A simple python script to create socket connections on server and accept data from client

# Import module SOCKET

import socket

# Create a TCP socket using socket() method. AF=Address Family, INET=Internet , SOCK_STREAM = a reliable connection?

TCPSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# Release the socket after connection terminated so that it can be reused immediately

TCPSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1  )

# Now let's bind this socket to a port and interface. Use bind() call

TCPSocket.bind( ( "0.0.0.0", 8000 ) )


# Now listen for incoming connections on port 8000 . use listen() call. Specify the number of connection you want to accept

TCPSocket.listen(2)

# Accept incoming connections. accept() returns a tuple . First element in the tuple is the client-side socket that is created once the client is connected
# Second element in the tuple holds the IP address of the client. So the third element holds the port number of the client.
# This will be used to connect to client. One client socket per client.

print "=" * 100

print " Ready to accept client connections.. "


# Accept incoming connections. accept() returns a tuple . First element in the tuple is the client-side socket that is created once the client is connected
# Second element in the tuple holds the IP address of the client. So the third element holds the port number of the client.
# This will be used to connect to client. One client socket per client.

print "=" * 100

print " Ready to accept client connections.. "

print "=" * 100
(client , ( ip, port )) = TCPSocket.accept()


# Print client information when client is connected

print " [*] Client with IP address %s and port number %d  is now connected " %(ip , port)


# Send welcome message to client using the client socket created on earlier

client.send(" Hello there! Welcome to the world of socket programming! ")

print  " I will now echo whatever client says"

# recieve data from client

data = "just a placeholder for now"

while len(data) :
        data = client.recv(2048)
        print "Client says: %s" % data
        client.send(data)

print " [*] Closing connection now"
client.close()
