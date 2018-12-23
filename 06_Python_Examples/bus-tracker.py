# This python code track the next bus to catch

import urllib3.request

u  = urllib3.request('http://ctabustracker.com/bustime/map/getStopPrediction.jsp?route=22&stop=14787')
data = u.read()

from xml.etree.ElementTree import XML
doc = XML(data)