#!/usr/bin/python
from struct import *
import sys
import socket
import time
import random
from optparse import OptionParser

data = pack('<HcBB', int(sys.argv[1],8), 'O', int(sys.argv[2]),int(sys.argv[3]))
s = socket.socket()         # Create a socket object
host = "10.38.18.105" # Get local machine name
port = 12345                # Reserve a port for your service.
s.connect((host, port))
s.send(data)
s.close
