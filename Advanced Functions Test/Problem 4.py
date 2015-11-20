# Problem 4
# Use zip and list comprehension to return a list of the same length where each value is the two strings from L1 and L2 
# concatenated together with connector between them. Look at the example output below:

def concatenate(L1, L2, connector):
    return zip(L1, L2)

print concatenate(['A','B'],['a','b'],'-')
# Expected output : ['A-a', 'B-b']