#!/usr/bin/python
from struct import *
import sys
import socket
import time
import random
from optparse import OptionParser
import ConfigParser
from random import randint

config = ConfigParser.RawConfigParser()
config.read('NrfUtils.conf')
s = socket.socket()         # Create a socket object
s.connect((config.get('NrfPiNode', 'hostname'), int(config.get('NrfPiNode', 'port'))))

sleeptime = 0.01

while 1:
    data = pack('<HcBBBBBB', int(sys.argv[1],8), 'W',0,int(sys.argv[2]),50,randint(0,255),randint(0,255),randint(0,255))
    s.send(data)
    time.sleep(sleeptime)
s.close
