things = [2, 5, 'nine', 22, True]

numbers = list(range(0, 11))

print(numbers, len(numbers))
# can use -1 to start from end
print(numbers[1+1], numbers[-1])
# Can check if 'nine' is in things list, Truthy Falsey
print('nine' in things)
# for loop
for thing in things:
    print('for looping ' + str(thing))
# how to while loop
index = 0
while index < len(things):
    print('while looping, '+str(things[index]))
    index += 1
