#!/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET - ipv4
#SOCK_STREAM - port
s.connect((HOST, PORT))

# In the command line -- establish a listening port on 7777 with netcat
# nc -nvlp 7777
# Waiting for someone to connect to it on port 7777

