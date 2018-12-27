
import csv

class Holding(object): 
    '''
    A collection of functions and the functions actually serve as methods
    one access through the . operation.
    '''

    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def cost(self): #define a cost method that carries out calculation
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

    def read_portfolio(self, filename):

        portfolio = []
        with open(filename, 'r') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                h = Holding(row[0], row[1], int(row[2]), float(row[3]))
                portfolio.append(h)
        return portfolio




# h = Holding('AA', '2012-12-26', 100, 34)
# h.name
# h.date
# h.shares
# h.cost()
# h.sell(10)
# h.shares

# There are majorly three things one can do with python object
#although it does has some consequences like `spelling errors` etc
# Another interesting thing about object is that methods are layered on the 
# get-set-del 
# The getattr and setattr functions open up a possibility of creating
# pretty generic piece of code 

# 1. Get an attribute h.name
# 2. Set an attribute  h.shares = 75
# 3. Delete an attribute del h.shares
