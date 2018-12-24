#! /usr/bin/env python3

'''
Handling bad data and exceptions
'''

import csv

def read_portfolio(filename, *, errors = 'warn'):

    '''
    Read a csv file with name, date, shares, price data into a list

    '''
    # defensive positions in function definitions

    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("Errors must be one of 'warn', 'silent', 'raise'")

    total = 0.0

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  #skip a single line of input

        for rownum, row in enumerate(rows, start = 1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', rownum, 'Bad row', row) 
                    print('Row:', rownum, 'Reason:', err)
                elif errors == 'raise':
                    raise       #reraises the last exception
                else:
                    pass        #Ignore

                continue        #skip to the next row

            total += row[2] * row[3]

    return total
total = portfolio_cost('../data/missing.csv', errors = 'silent')
print('Total cost:', total)