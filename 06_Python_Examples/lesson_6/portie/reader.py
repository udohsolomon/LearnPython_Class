#!/usr/bin/env python3

import csv

def read_csv(filename, types, *, errors = 'warn'):
    '''
    Read a CSV file with type conversion into a list of dicts as a basis for 
    writing a more general library.
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
                '''
                   A row of data where the types have been converted
                   after pairing up a type conversion with a value 
                   using the zip function
                '''
                
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', rownum, 'Bad row', row) 
                    print('Row:', rownum, 'Reason:', err)
                elif errors == 'raise':
                    raise       #reraises the last exception
                else:
                    pass        #ignore

                continue        #skip to the next row
            record = dict(zip(headers, row)) #A dictionary of converted value
            records.append(record)
    return records