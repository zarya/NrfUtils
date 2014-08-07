#!/usr/bin/python
from struct import *
import sys
import socket
import time
import random
from optparse import OptionParser
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('NrfUtils.conf')
s = socket.socket()         # Create a socket object
s.connect((config.get('NrfPiNode', 'hostname'), int(config.get('NrfPiNode', 'port'))))

for i in range(0,255):
    data = pack('<HcBBBB', int(sys.argv[1],8), 'W',int(sys.argv[2]),i,i,i)
    s.send(data)
    time.sleep(0.05)

for y in reversed(range(0,255)):
    data = pack('<HcBBBB', int(sys.argv[1],8), 'W',int(sys.argv[2]),y,y,y)
    s.send(data)
    time.sleep(0.05)
s.close
