#!/usr/bin/python
from struct import *
import sys
import socket
import time
import random
from optparse import OptionParser
import ConfigParser
import os

config = ConfigParser.RawConfigParser()
config.read('NrfUtils.conf')

storage = {} 

s = socket.socket()         # Create a socket object
s.connect((config.get('NrfPiNode', 'hostname'), int(config.get('NrfPiNode', 'port'))))

def draw(storage):
    os.system('clear')
    print "Node\tLast\tInterval\tBattery"
    for k, v in sorted(storage.iteritems()):
        nodeid = k
        oldts = v['bts']-v['oldts']
        if oldts < 10000:
            oldts = "%s\t"%oldts
        if v['oldts'] == 0:
            oldts = "\t"
        if float(v['batv']) == 0:
            print "%s\t%s\t\t\tNa"%(nodeid,int(time.time()-v['ts']))
        else:
            print "%s\t%s\t%s\t%0.2f (failure in %0.2f)"%(nodeid,int(time.time()-v['ts']),oldts,float(v['batv']),float(v['batv']) - 3.00)

while 1:
    data = s.recv(64)
    value = data.split()[1]
    sensor = data.split()[0].split('.')
    if storage.get(sensor[2],False):
        oldts = storage[str(sensor[2])]['bts']
    else:
        storage[sensor[2]] = {'batv':0,'ts':int(time.time()),'oldts':0,'bts':0}
    storage[str(sensor[2])]['ts'] = int(time.time()) 
    if sensor[3] == "B":
        storage[str(sensor[2])]['oldts'] = oldts
        storage[str(sensor[2])]['bts'] = int(time.time()) 
        storage[sensor[2]]['batv'] = value
    draw(storage)
    error = False
