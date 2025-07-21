#working directory - !/usr/bin/python

import socket

#socket.socket() - denotes function(object), socket.AF_INET - denotes IPv4(socket family), socket.SOCK_STREAM - denotes TCP connection(socket type)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#function grabs nost name and other specified info
host = socket.gethostname()
port = 444

#function binds host and port to serversocket object
serverSocket.bind((host, port))

#function allows device to listen to specified amount of connections
serverSocket.listen(2)

while True:
     clientSocket, address = serverSocket.accept()

     print('Connection received from %s ' % str(address))

     message = ' Thank you for connectiong to the server' + '\r\n'
     clientSocket.send(message.encode('ascii'))

     clientSocket.close()