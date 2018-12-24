#! /usr/bin/env python3

'''
Find out how much to pay off a mortgage

'''

# Declare variables
principal = 500000
payment = 2684.11
rate = 0.05
total_paid = 0

# Extra payment info
extral_payment = 1000
extral_payment_start_month = 1
extral_payment_end_month = 60
month = 0

while principal > 0:
    month += 1
    if month >= extral_payment_start_month and month <= extral_payment_end_month:
        total_payment = payment + extral_payment
    else:
        total_payment = payment
        
    interest = principal * (rate/12)
    principal = principal + interest - total_payment
    total_paid += total_payment

print('Total paid:', total_paid)

