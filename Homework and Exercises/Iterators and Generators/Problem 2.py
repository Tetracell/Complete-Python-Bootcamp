# Problem 2
# Create a generator that yields "n" random numbers between a low and high number 
# (that are inputs). Note: Use the random library.

import random

def rand_num(low, high, n):
    while n > 0:
        yield random.randint(low, high)
        n -= 1

for num in rand_num(1,10,12):
    print num


