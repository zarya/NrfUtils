#!/usr/bin/python
from struct import *
import sys
import socket
import time
import random
from optparse import OptionParser

current_milli_time = lambda: int(round(time.time() * 1000))

if sys.argv[1]is None:
    print "run like `ping.py 5`"
    sys.exit(1)

nodeaddress = "%o" % int(sys.argv[1],8)
if nodeaddress.find("0") != -1 or nodeaddress.find("6") != -1 or nodeaddress.find("7") != -1:
    print "Invalid node address"
    sys.exit(1)
ping_id = random.randrange(0, 9999)
current_time = current_milli_time()
data = pack('<HcH', int(sys.argv[1],8), 'P', ping_id)
s = socket.socket()         # Create a socket object
host = "10.38.18.105" # Get local machine name
port = 12345                # Reserve a port for your service.
s.connect((host, port))
s.send(data)
while 1:
    data = s.recv(64)
    now_time = current_milli_time()
    if data[:1] == "Q":
        reply = data.split()
        if int(reply[2]) == ping_id:
            reply_time = now_time - current_time
            print "Reply from node: %o ttl: %i ms." % (int(reply[1]),reply_time)
            break
    if (now_time - current_time) > 9000:
        print "Ping timeout"
        break 
s.close
