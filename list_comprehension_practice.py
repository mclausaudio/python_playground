# Given a list, make a var called answer,
# which is a new list containing the first letter of each name in the list.
friends = ['Renee', 'Sepehr', 'Moon', 'Miles']
answer = [friend[0] for friend in friends]
print(answer)

# Write a short program that prints each number from 1 to 100 on a new line.

# For each multiple of 3, print "Fizz" instead of the number.

# For each multiple of 5, print "Buzz" instead of the number.

# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
nums = list(range(1, 21))
print(nums)
print([
    'fizzbuzz' if num % 3 == 0 and num % 5 == 0
    else 'fizz' if num % 3 == 0
    else 'buzz' if num % 5 == 0
    else num
    for num in nums])

# worth noting that this would be much better as a loop/function
# but this is for proof of concept with list comprehension
# also inside the list comprehension, no if elif, just elses
