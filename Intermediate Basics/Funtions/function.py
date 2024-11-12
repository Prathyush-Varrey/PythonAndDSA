''' 
In Python, functions are reusable blocks of code designed to perform specific tasks.
They help you organize code, avoid repetition, and make your programs more modular
and readable.

Defining a Function
In Python, you define a function using the def keyword, followed by the function 
name and parentheses (). Parameters (inputs) go inside the parentheses, and the 
function's code block is indented.


def function_name(parameters):
    # Code to execute
    return result  # Optional

'''
def add(a, b):
     """ Adds 2 values and returns their Result"""
     return a + b

# print(add(1,2))

# Types of Functions
# without Parameters
def greet1():
     print('hello')
greet1()

# Functions with Parameters
def greet2(name):
    print(f"Hello, {name}!")

greet2("Alice")  # Output: Hello, Alice!

# Functions with Default Parameters
def greet3(name="World"):
    print(f"Hello, {name}!")

greet3()         # Output: Hello, World!
greet3("Alice")  # Output: Hello, Alice!


# Functions with Return Values
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print(result)  # Output: 12

# Lambda Functions
add = lambda x, y: x + y
print(add(5, 7))  # Output: 12
