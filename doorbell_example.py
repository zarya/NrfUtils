#!/usr/bin/python
from struct import *
import sys
import socket
import time
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('NrfUtils.conf')

s = socket.socket()         # Create a socket object
s.connect((config.get('NrfPiNode', 'hostname'), int(config.get('NrfPiNode', 'port'))))
while 1:
    data = s.recv(64)
    if data.split()[0] == "sensor.net.5.P.0":
        print "DING DONG"
s.close
