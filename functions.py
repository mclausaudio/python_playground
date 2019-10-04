import math

praise = "Great times"


def yell(text):
    text = text.upper()
    # Remember // returns an int, not a float
    result = text + "!" * (len(text) // 2)
    print(result)


yell(praise)


def split_check(total, number_of_people):
    if number_of_people <= 1:
        # throws a value error
        raise ValueError("More than 1 person is required to split a check.")
    return math.ceil(total / number_of_people)  # math.ceil rounds up


# try, except (type of error), else. Similar to Try / Catch in JavaScript
# try this block of code, if a ValueError error occurs run the code in except, if no errors (else) then print the function return
try:
    grand_total = float(input("What is the total?"))
    number_of_people = int(input("How many people?"))
    amount_due = split_check(grand_total, number_of_people)
except ValueError as err:
    print("Something happened! That's not a valid value")
    print("({})".format(err))
else:
    print(amount_due)
