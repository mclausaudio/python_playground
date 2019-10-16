# [ EXPRESSION for PLACEHOLDER_VAR in LIST ]
# returns a NEW string, does not modify existing
nums = [1, 2, 3]
print([x*10 for x in nums])
print([x/2 for x in nums])
# List comprehension is much cleaner than using a for loop.
# Below is the same as [x*2 for x in nums]
doubled_nums = []
for num in nums:
    doubled_nums.append(num*2)
print(doubled_nums)
# clearly list comprehension is cleaner, more concise.
# Can use with strings
name = "michael"
print([letter.upper() for letter in name])
print(''.join([letter.upper() for letter in name]))
# example of upercasing each string in array
friends = ['renee', 'sepehr', 'miles', 'sebastian']
print([friend.title() for friend in friends])
print([(friend[0].upper() + friend[1:]) for friend in friends])
# more examples
# range(1, 6) generates numbers 1 through 5
print([num*10 for num in range(1, 6)])
# outputs boolean representation of list values
print([bool(val) for val in [0, '', 22, [], 'stringy']])
# CONVERTING DATA TYPES!
# convert numbers to strings
print([str(num) for num in nums])
