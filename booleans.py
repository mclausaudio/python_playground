# Booleansa
print(
    bool('Michael')  # => True
)

print(
    bool(42)  # => True
)

# Emptiness is Falsey
print(
    bool("")  # => False
)

# can negate with the 'not' keyoword.  Similar to ! in JavaScript
print(not True)  # => False
print(not False)  # => True

# 'and' keyword.. evaluates True if all expressions evaluate to true
print(True and True and True)  # => True
print(True and False and True)  # => False

# 'or' statement, evaluates True if one expression evaluates True
print(True or False)  # => True
# can group statements with ()'s
print((False or False or True) and (not False and True))  # => True

is_programming = True
at_laptop = True
print(at_laptop and not is_programming)  # => False
