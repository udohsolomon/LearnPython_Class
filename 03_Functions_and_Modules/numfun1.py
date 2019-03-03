"""
small demo of modules
"""

## do some stuff and set some variables
print("numfun1 in the house")
x    = 2
s    = "spam"

def numop(x, y, multiplier = 1.0, greetings = "Thank you for your inquiry."):
    """ 
Purpose: does a simple operation on two numbers. 

Input: We expect x,y are numbers 
       multiplier is also a number (a float is preferred) and is optional.  
       It defaults to 1.0. You can also specify a small greeting as a string.

Output: return x + y times the multiplier
    """
    if greetings is not None:
          print(greetings)
    return (x + y)*multiplier