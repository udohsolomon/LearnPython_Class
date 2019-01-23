
# Set some initial variables. Set the initial temperature low

faren = -500

# We don't want the number of attempts going on forever, let's make sure we can't have too many attempts

max_attempts = 5
attempts = 0

while faren < 100:
    # Let's get the user to tell us what temperature it is
    newfaren = float(input('Enter the temperature value (in Fahrenheit): '))
    if newfaren > faren:
        print('It\'s getting hotter')
    elif newfaren < faren:
        print('It\'s getting cooler')
    else:
        # nothing has changed, just continue in the loop
        continue
    faren = newfaren # now set the current temperature to the new temperature just entered
    attempts += 1 # Now bunp up the attempt number
    if attempts >= max_attempts:
              # We have to bail out ):
              break
if attempts >= max_attempts:
    # We bailed out because of too many attempts
    print('Too many attempts at raising the temperature')
else:
    # We got here because it's too hot
    print('It\'s too hot here people!')
              
              
