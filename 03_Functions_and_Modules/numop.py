
"""
Some functions written to demonstrate a bunch of concepts like modules, 
import, and command-line programming.

"""

def numop(x, y, multiplier = 1.0, greetings = 'Thank you for your inquiry.'):
    
    '''numop -- this does a simple operation on two numbers. 
     We expect x,y are numbers and return x + y times the multiplier
     multiplier is also a number (a float is preferred) and is optional. 
     It defaults to 1.0.
     You can also specify a small greeting as a string.
     
    '''
    
    if greetings is not None:
        
        print(greetings)
        
    return (x + y) * multiplier