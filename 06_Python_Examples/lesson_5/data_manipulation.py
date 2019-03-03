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
names = [holding['name'] for holding in portfolio]
more100 = [holding for holding in portfolio if holding['shares'] > 100]

# getting the current stock prices of these stocks
# unique_names = set(names)
# namestr = ','.join(unique_names)
# import urllib.request
# u = urllib.request.urlopen('http://finance.yahoo.com/d/quotes.csv?s={}&f=l1'.format(namestr))
# data = u.read()

# Sorting and Grouping

def holding_name(holding):
    return holding['name']

holding_name(portfolio[0])
portfolio.sort(key = holding_name)
for holding in portfolio:
    print(holding)