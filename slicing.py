# list slicing
# list_to_slice[start_index:end_index:interval]
# does not modify original list directly, returns a copy that can be assigned to variable

first_list = [1, 2, 3, 4, 5]

# putting just index returns that index value
print("first_list[1]")
print(first_list[1])
# adding the : initiaes a slice
print("first_list[1:]")
print(first_list[1:])
# can slice from end with negative numbers
print("first_list[-2:]")
print(first_list[-2:])
# the end index is EXCLUSIVE, does not include
# slices UP UNTIL TO
print("first_list[1:3]")
print(first_list[1:4])
# canuse negative value for end index to represent end of list
# remember, end index is EXCLUSIVE, so -1 cuts off the last value
print("first_list[1:-1]")
print(first_list[1:-1])
# can utilize the step to skip over the list.. for example "only grab every second"
# don't need to include value if it is 'default'
# meaning 0 for start, last for end. just need to include the :
print("first_list[0::2]")
print(first_list[0::2])
# can use negative numbers, with negative steps, the end default is 0
print("first_list[3::-2]")
print(first_list[3::-2])
print("first_list[::-2]")
print(first_list[::-2])
# can be used to modify string
print('first_list[1:3]=["Michael", "J", "Claus"]')
first_list[1:3] = ["Michael", "J", "Claus"]
print(first_list)
# these can be used on strings
# reverse a string
string = "Michael"
print(string[::-1])
# or reverse a string of a list
print('first_list[1] = first_list[1][::-1]')
first_list[1] = first_list[1][::-1]
print(first_list)
# does not modify original list directly
print("first_list")
print(first_list)
