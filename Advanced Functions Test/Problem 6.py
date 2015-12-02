# Problem 6
# Use enumerate and other skills from above to return the count of the number 
# of items in the list whose value equals its index.


def count_match_index(L):
    similarity = 0
    for index, number in enumerate(L):
        if index == number:
            similarity += 1
    return similarity

def count_match_index_2(L):
    return

print count_match_index([0,2,2,1,5,5,6,10])
print count_match_index_2([0,2,2,1,5,5,6,10])
# Expected output : 4