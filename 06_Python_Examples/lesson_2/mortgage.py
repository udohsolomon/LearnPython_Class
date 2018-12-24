#! /usr/bin/env python3

'''
Find out how much to pay off a mortgage

'''

# Declare variables
principal = 500000
payment = 2684.11
rate = 0.05
total_paid = 0

while principal > 0:
    interest = principal * (rate/12)
    principal = principal + interest - payment
    total_paid += payment

print('Total paid:', total_paid)

