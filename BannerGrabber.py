import socket

s = socket.socket()

ip = input("Enter the IP: ")
port = str(input("Enter the port: "))

s.connect((ip, int(port)))
print(s.recv(1024))