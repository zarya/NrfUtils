#!/usr/bin/python
from struct import *
import sys
import socket
import time
from optparse import OptionParser

current_milli_time = lambda: int(round(time.time() * 1000))

if sys.argv[1]is None:
    print "run like `ping.py 5`"
    sys.exit(1)


current_time = int(str(current_milli_time())[-4:])
data = pack('<HcH', int(sys.argv[1]), 'P', current_time)
s = socket.socket()         # Create a socket object
host = "10.38.18.105" # Get local machine name
port = 12345                # Reserve a port for your service.
s.connect((host, port))
s.send(data)
while 1:
    data = s.recv(64)
    if data[:1] == "Q":
        reply = data.split()
        current_time = int(str(current_milli_time())[-4:])
        reply_time = current_time - int(reply[2])
        print "Reply from node: %s ttl: %s ms." % (reply[1],reply[2])
        break 
s.close
