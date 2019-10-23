fish1 = {"name": "blue", "type": "tetra", "color": "blue", "size": "small"}
fish2 = dict(name="star", type="betta")
print(fish1)
print(fish2["name"])
# the .value() dictionary method returns a list of values
print(fish1.values())
# the .keys() dictionary method returns a list of keys
print(fish1.keys())
# can loop over these if you'd like
for k in fish1.keys():
    print(k)
for v in fish1.values():
    print(v)
# to get both, we use .items() method... returns tuples which are kind of like immutable lists
# dictionary looping requires two variables in for loop
for k, v in fish1.items():
    print(f"the {k} key has a value of {v}")
# the 3 most common methods, .keys() .values() .items()

# we can use 'in' to check if a dictionary contains a specific KEY
print('age' in fish1)  # False
# this only works for keys.. this defaults to testing dictionary.keys()
# in order to test if a dictionary contains a value,
#  we do the following:
print('blue' in fish1.values())  # True
# more methods
# .clear() empties dictionary
print('.clear()')
fish1.clear()
print(fish1)
# .copy() copies another dictionary to a new variable and stores it into a new palce in memory
fish3 = fish2.copy()
print(fish3)
print(fish3 is fish2)  # False
# can create / add key value pairs with .fromkeys()
# must pass key (or multiple keys) in as a list, or it tries to iterate over the string
newUser = {}.fromkeys(["name", "score", "email"], None)
# commonly used for creating default values
print(newUser)
