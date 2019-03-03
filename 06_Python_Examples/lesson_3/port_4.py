#! /usr/bin/env python3
import csv
import glob
from port_3 import portfolio_cost

files = glob.glob('../data/portfolio*.csv')
for filename in files:
    print(filename, portfolio_cost(filename))

