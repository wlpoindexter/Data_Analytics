# ValueError Example
try:
    age = int("twenty")
except ValueError:
    print("ValueError: Cannot convert text to a number.")
else:
    print(age)
finally:
    print("Let's try another one...\n")


# NameError Example
try:
    print(banana)
except NameError:
    print("NameError: Variable does not exist.")
else:
    print(banana)
finally:
    print("Let's try another one...\n")


# TypeError Example
try:
    total = "5" + 5
except TypeError:
    print("TypeError: Cannot add a string and an integer.")
else:
    print(total)
finally:
    print("Let's try another one...\n")


# SyntaxError Example
try:
    exec("if True print('Hello')")
except SyntaxError:
    print("SyntaxError: Invalid Python syntax.")
else:
    print("No error occurred.")
finally:
    print("Let's try another one...\n")