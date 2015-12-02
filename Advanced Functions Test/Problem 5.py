# Problem 5
# Use enumerate and other skills to return a dictionary which has the values of the 
# list as keys and the index as the value. You may assume that a value will only appear 
# once in the given list.

def d_list(L):
    dict = {}
    for number, item in enumerate(L):
        dict[item] = number
    return dict

print d_list(['a','b','c'])
#Expected output: {'a': 0, 'b': 1, 'c': 2}