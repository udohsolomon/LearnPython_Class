#!/usr/bin/env python3

# This python code tracks the next bus to catch
import sys

if len(sys.argv) != 3:
    raise SystemExit('Usage: bus_tracker_modified.py route stopid')

route = sys.argv[1]
stopid = sys.argv[2]

# print('Command options', sys.argv)
# raise SystemExit(0)
import urllib.request


u  = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPrediction.jsp?route={}&stop={}'.format(route, stopid))

#import pdb; pdb.set_trace() #Launch debugger
data = u.read()

#print('Response:', data) # Use print statement for debugging

from xml.etree.ElementTree import XML
doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.text)

#python3 -i bus_tracker_debug.py
#import pdb 
#pdb.pm()