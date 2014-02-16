#!/usr/bin/python

import sys

if sys.argv[1]is None:
    print "run like `nodeid_to_address.py 72`"
    sys.exit(1)

nodeaddress = "%o" % int(sys.argv[1])
if nodeaddress.endswith("0"):
    print "Invalid address"
    sys.exit(1)
print "Address: %o" % int(sys.argv[1])
