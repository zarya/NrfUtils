#!/usr/bin/python
from struct import *
import sys
import socket
import time
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--node", dest="node", type="int",
                  help="Node id")
(options, args) = parser.parse_args()

if options.node is None:
    print "Run 'ping.py -h' for options."
    sys.exit(1)


#data = pack('Hc77s', 5, 'C', "")
data = pack('HcI', int(options.node), 'P', int(time.time()))
s = socket.socket()         # Create a socket object
host = "10.38.18.105" # Get local machine name
port = 12345                # Reserve a port for your service.
s.connect((host, port))
s.send(data)
while 1:
    data = s.recv(64)
    if data[:1] == "Q":
        reply = data.split()
        print "Reply from %s ttl: %s" % (reply[1],reply[2])
        break 
s.close
