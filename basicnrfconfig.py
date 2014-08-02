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

data = pack('<HcBB', int(sys.argv[1],8), 'C', int(sys.argv[2]),int(sys.argv[3]))
s = socket.socket()         # Create a socket object
s.connect((config.get('NrfPiNode', 'hostname'), int(config.get('NrfPiNode', 'port'))))
s.send(data)
s.close
