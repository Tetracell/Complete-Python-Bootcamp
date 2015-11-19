# Problem 1
# Use map to create a function which finds the length of each word in the phrase (broken by spaces) and return the values in a list.
# The function will have an input of a string, and output a list of integers

def word_lengths(phrase):
    #map(lambda w: len(w), phrase.split())
    #lst = phrase.split()
    #word_len = [len(x) for x in lst]
    # Alternatively, map(len, phrase.split()) would also work because len is itself a function?
    return map(lambda w: len(w), phrase.split())
    

print word_lengths('How long are the words in this phrase')
# Expected output: [3, 4, 3, 3, 5, 2, 4, 6]
