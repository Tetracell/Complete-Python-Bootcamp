# Problem 2
# Use reduce to take a list of digits and return the number that they correspond to. 
# Do not convert the integers to strings!

def digits_to_num(digits):
    return reduce(lambda x,y: x*10 + y,digits) # Completely failed at coming up with this solution. Thought
                                               # of multiplying first number by 10, and stalled afterward.

digits_to_num([3,4,3,2,1])