nested_list = [[1, 2, 3], [4, 5, 6], [6, 7, 8]]

print(nested_list[-1][1])
# nested for loops
print('nested for loops')
for l in nested_list:
    for val in l:
        print(val)
print('nested list comprehension')
# nested list comprehension
[[print(val) for val in l] for l in nested_list]
# creating nested list with list comprehension
created = [[val for val in range(1, 4)] for val in range(0, 3)]
print(created)
board = [["X" if num % 2 == 0 else "O" for num in range(
    0, 3)] for val in range(0, 3)]
print(board)
nest = [[i for i in range(0, 3)] for num in range(0, 3)]
print(nest)
