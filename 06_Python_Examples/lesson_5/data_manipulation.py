from data_structure import read_portfolio

portfolio = read_portfolio('../data/portfolio.csv')

for holding in portfolio:
    print(holding)

#filtering by name only
name = []
for holding in portfolio:
    name.append(holding['name'])

name

# filtering by number of shares greater than $100

more_100 = []
for holding in portfolio:
    if holding['shares'] > 100:
        more_100.append(holding)
more_100

# List comprehension

total = sum([holding['shares'] * holding['price'] for holding in portfolio])