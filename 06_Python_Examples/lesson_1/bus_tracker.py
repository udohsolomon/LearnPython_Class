#!/usr/bin/env python3
# This python code track the next bus to catch

import urllib.request

u  = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route=22&stop=14787')
data = u.read()

from xml.etree.ElementTree import XML
doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.text)