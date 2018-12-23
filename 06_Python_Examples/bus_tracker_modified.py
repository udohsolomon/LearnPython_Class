# This python code track the next bus to catch
import sys
import urllib.request

if len(sys.argv != 3):
    raise SystemExit('Usage: bus_tracker_modified.py route stopid')

route = sys.argv[1]
stopid = sys.argv[2]

print('Command options', sys.argv)
raise SystemExit(0)

u  = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}',format(\
route, stopid))
data = u.read()

from xml.etree.ElementTree import XML
doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.text)