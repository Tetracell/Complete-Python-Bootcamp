# Problem 3
# Use the iter() function to convert the string below 

s = 'hello'
s_iter = iter(s)

print next(s_iter)
for i in range(len(s)):
    print next (s_iter)
