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

data = pack('<HcBBBBBB', int(sys.argv[1],8), 'W',int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5],16),int(sys.argv[6],16),int(sys.argv[7],16))
s = socket.socket()         # Create a socket object
s.connect((config.get('NrfPiNode', 'hostname'), int(config.get('NrfPiNode', 'port'))))
s.send(data)
s.close
