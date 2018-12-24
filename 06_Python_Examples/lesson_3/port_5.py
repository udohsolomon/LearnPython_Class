#! /usr/bin/env python3

'''
Handling bad data and exceptions
'''

import csv

def portfolio_cost(filename):

    '''
    Computes total shares * price for a csv file with name, date, shares, price data

    '''

    total = 0.0

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  #skip a single line of input

        for rownum, row in enumerate(rows, start = 1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                print('Row:', rownum, 'Bad row', row)
                print('Row:', rownum, 'Reason:', err)

                continue    #skip to the next row

            total += row[2] * row[3]

    return total
total = portfolio_cost('../data/missing.csv')
print('Total cost:', total)