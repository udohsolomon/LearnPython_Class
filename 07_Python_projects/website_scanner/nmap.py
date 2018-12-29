import os

def get_nmap(option, ip):
    command = 'nmap ' + option + ' ' + ip
    process = os.popen(command)
    results = str(process.read())
    return results