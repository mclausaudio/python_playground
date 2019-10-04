# if, elif, else
# comparions... ==, !=, >, <, >=, <=,
name = input('What is your name? ')
if name == "Michael":
    print('Yes, name == "Michael')
elif name == "Renee":
    print('Yes, name == Renee')
else:
    print('No, name is not Michael or Renee. In fact, it is {}'.format(name))


if name != "Michael":
    print('The name is not Michael')
