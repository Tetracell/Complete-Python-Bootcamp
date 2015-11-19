# Problem 3
# Use filter to return the words from a list of words which start with a target letter.

def filter_words(word_list, letter):
    return filter(lambda word: word[0] == letter , word_list) 

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print filter_words(l,'h')