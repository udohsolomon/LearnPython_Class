import os

def get_nmap(option, ip):
    command = 'nmap ' + option + ' ' + ip