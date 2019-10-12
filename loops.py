for i in 'michael':
    print(i*5)

# range(start, end(not included), interval(optional))
for i in range(0, 5, 2):
    print(i)

for i in range(8, 0, -2):
    print(i)

times = input('How many times would you like to loop: ')
for i in range(1, int(times)+1):
    print('for looping ' + str(i) + ' times')

num = 1
while num <= int(times):
    print('while looping '+str(num))
    num += 1

# can use 'break' keyword to exit loop early.
