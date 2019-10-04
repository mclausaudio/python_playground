first_name = input('What is your first name? ')

print('Hello,', first_name)

# prints length.. like .length
len(first_name)

print('The length of first_name is', len(first_name))

# A few built in string methods
print(first_name.upper())
print(first_name.lower())
print(first_name.title())

#  convert string to int and vice versa
print(str(42))  # str for string
print(int('42'))  # int for integer

# can pass data types into a help() for more info
help(str)
# press Q to drop out of help menu

# format templates, write a string and use {} as a 'placeholder'
phrase = "Good job, {}. Keep studying {}."
# use .format method to 'inject' value into placeholders
phrase.format(first_name, "Python")
print(phrase.format(first_name, "Python"))
# OR write a string and tack on .format()
print('This is a {} that was written by {}'.format('string', first_name))

# Can check is a string contains a substring, below returns boolean
print("Py" in "Python")  # => True
print("py" in "Python")  # => False... case matters
# => True, assuming "Michael" is assigned to first name
print("ael" in first_name)
