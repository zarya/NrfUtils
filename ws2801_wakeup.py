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

sleeptime = 0.05

for i in range(0,255):
    data = pack('<HcBBBBBB', int(sys.argv[1],8), 'W',0,int(sys.argv[2]),50,i,i,i)
    s.send(data)
    time.sleep(sleeptime)

for y in reversed(range(0,255)):
    data = pack('<HcBBBBBB', int(sys.argv[1],8), 'W',0,int(sys.argv[2]),50,y,y,y)
    s.send(data)
    time.sleep(sleeptime)
s.close
