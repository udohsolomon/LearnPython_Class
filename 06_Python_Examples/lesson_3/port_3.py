#! /usr/bin/env python3
import csv

def portfolio_cost(filename):

    '''
    Computes total shares * price for a csv file with name, date, shares, price data

    '''

    total = 0.0

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  #skip a single line of input
        for row in rows:

            row[2] = int(row[2])
            row[3] = float(row[3])
            total += row[2] * row[3]

    return total
total = portfolio_cost('../data/portfolio.csv')
print('Total cost:', total)