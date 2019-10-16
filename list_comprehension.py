# [ EXPRESSION for PLACEHOLDER_VAR in LIST ]
# returns a NEW string, does not modify existing
nums = [1, 2, 3, 4, 5]
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
# Conditional logic
# can add an if statement at the end
print('even numbers', [num for num in nums if num % 2 == 0])
print('odd numbers', [num for num in nums if num % 2 != 0])
# can add an else statement, but must move condition to the front.. in the expression
# below multiplies num by 2 if even, divides if odd.
print([num*2 if num % 2 == 0 else num / 2 for num in nums])
# more strings
with_vowels = "python is awesome"
# so basically this is saying return char without doing anything, char is the placeholder
# for each letter in the with_vowels string, only if that char is not in the 'aeiou' string
no_vowels = ''.join([char for char in with_vowels if char not in 'aeiou'])
print(no_vowels)
