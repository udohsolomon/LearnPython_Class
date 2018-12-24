#!/usr/bin/env python3

import csv

def read_csv(filename, types, *, errors = 'warn'):
    '''
    Read a CSV file with type conversion into a list of dicts
    '''
    # defensive positions in function definitions

    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("Errors must be one of 'warn', 'silent', 'raise'")

    records = []

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  #skip a single line of input

        for rownum, row in enumerate(rows, start = 1):
            try:
                row = [ func(val) for func, val in zip(types, row)]
                
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', rownum, 'Bad row', row) 
                    print('Row:', rownum, 'Reason:', err)
                elif errors == 'raise':
                    raise       #reraises the last exception
                else:
                    pass        #Ignore

                continue        #skip to the next row
            record = dict(zip(headers, row))
            records.append(record)
    return records