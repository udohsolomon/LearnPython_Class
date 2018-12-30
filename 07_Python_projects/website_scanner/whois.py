import os

def get_whois(url):
    command = 'whois ' + url
    process = os.popen(url)
    results = str(process.read())

