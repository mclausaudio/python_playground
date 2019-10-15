things = [2, 5, 'nine', 22]

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


# LIST METHODS
print("LIST METHODS")
print("LIST METHODS")
print("LIST METHODS")

print("Things, " + str(things))
# .append adds a single value and takes only a single argument
things.append("appended")
print("after append, " + str(things))
# .extend takes a single argument, a list of things to add to the list.
# must be a single list of things to add
things.extend(["extend 1", "extend 3"])
print("after extend, " + str(things))
# inserts an item into a list.  first argument is the index, second argument is the value
things.insert(2, 'inserted')
# can use negative numbers to insert from the end of list..
# takes the original array and goes backwards from there, so -1 is the second to last index
# if you want to put something at the end just use .append.. but could technically do list.insert(len(list), value)
things.insert(-1, '-1 inserted')
print("after insert, " + str(things))
# .pop removes a single element from list.. takes a single argument, the index to be removed
# this will RETURN the popped value - important to note
print('Popped value is... ' + str(things.pop(3)))
# when no arguments passed, removes last index by default
things.pop()
print("after pop, " + str(things))
# .remove removes the first item from the list whose value is x
# throws ValueError if item not found
things.remove('extend 1')
print("after remove, " + str(things))
# .index returns index of specific value, passed in as argument.
# takes an optional second argument that specifies index to start searching at
# below looks for the index value of 22 after the 2 index, good to use to ignore certain portions of list
print('.index of 22 ' + str(things.index(22, 2)))
# .count returns number of times a value (the argument passed in) occurs in a list
print('.count ' + str(things.count(4)))  # returns 0 becuase not in list
# .reverse reverses list in-place, so it reverses the original list, does not return anyhting
things.reverse()
print('after .reverse ' + str(things))
# .join is actually a string method, but commonly used to make lists into strings
# only argument is the list
sentence = ', '.join(str(things))
print('The things are as follows ' + sentence)
# .clear removes all items from list.. less common.  takes no arguments
things.clear()
print("after clear, " + str(things))
