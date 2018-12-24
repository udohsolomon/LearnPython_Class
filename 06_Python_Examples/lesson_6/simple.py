#!/usr/bin/env python3

# simple.py

x = 42

def spam():
    print('x is', x)

def run():
    print('Calling the new spam')
    spam()

if __name__ == '__main__': # check to see if module is the main program or not
    print('Running')
    run()