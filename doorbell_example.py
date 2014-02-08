#!/usr/bin/python
from struct import *
import sys
import socket
import time

s = socket.socket()         # Create a socket object
host = "10.38.18.105" # Get local machine name
port = 12345                # Reserve a port for your service.
s.connect((host, port))
while 1:
    data = s.recv(64)
    if data.split()[0] == "sensor.net.5.P.0":
        print "DING DONG"
s.close
