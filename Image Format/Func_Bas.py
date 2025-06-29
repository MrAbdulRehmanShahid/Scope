# 1. Function Basics
def greet(name):
    print(f"Hello, {name} How are you doing?")

greet("Flora")
# 2. Return Values
def square(num):
    return num * num
print("The square of 6 is:", square(6))
# 3. Function with  Multiple Parameters
def add (a,b):
    return a + b
print("The sum of 583 and 389 is:", add(583, 389))
# 4. Default Arguments
def greet(name= "Guest"):
    print(f"Hello, {name} How are you doing?")
greet()   
# 5. Combined Challenge
def is_even(num):
    """Check if a number is even."""
    return num % 2 == 0

print(is_even(9)) # Output: False
print(is_even(6)) # Output: True 


  
# def calculate(n1,n2, operation="add"):
#     """Perform a calculation based on the operation."""
#     if operation == "add":
#         return n1 + n2
#     elif operation == "subtract":
#         return n1 - n2
#     elif operation == "multiply":
#         return n1 * n2
#     elif operation == "divide":
#         return n1 / n2
#     else:
#         raise ValueError("Invalid operation")

# print("Output is:" ,calculate(83, 71))# Output: 154
# print("Output is:" ,calculate(57, 31, "subtract")) # Output: 26
# print("Output is:" ,calculate(8, 9, "multiply")) # Output: 72
from typing import Union
def calculate_with_union(n1: float, n2: float, operation: str = "add") -> Union[float, ValueError]:
    """Perform a calculation based on the operation with type hints."""
    if operation == "add":
        return n1 + n2
    elif operation == "subtract":
        return n1 - n2
    elif operation == "multiply":
        return n1 * n2
    elif operation == "divide":
        if n2 == 0:
            raise ValueError("Cannot divide by zero")
        return n1 / n2
    else:
        raise ValueError("Invalid operation")
    
# OPERATIONS = {
#     "add": lambda a, b: a + b,
#     "subtract": lambda a, b: a - b,
#     "multiply": lambda a, b: a * b,
#     "divide": lambda a,b : a / b if b!= 0 else ValueError("Cannot divide by zero"),
#     # "modulus": lambda a, b: a % b,  # Uncomment if you want to include modulus operation
#     # "power": lambda a, b: a ** b,  # Uncomment if you want to include power operation
    # "floor_divide": lambda a, b: a // b,  # Uncomment if you want to include floor division
    # "absolute": lambda a: abs(a),  # Uncomment if you want to include absolute value operation
    # "negate": lambda a: -a,  # Uncomment if you want to   include negation operation
    # "factorial": lambda a: math.factorial(a),  # Uncomment if you want to include factorial operation
    # "square_root": lambda a: math.sqrt(a),  # Uncomment if you want   to include square root operation
    # "logarithm": lambda a, b: math.log(a, b), # Uncomment if you want to include logarithm operation 
    # ... etc ...
# }

# def calculate_with_operations(n1, n2, operation="add"):
#     if operation not in OPERATIONS:
#         raise ValueError("Invalid operation")
#     return OPERATIONS[operation](n1, n2)
# print(calculate_with_operations(56, 93))
# print(calculate_with_operations(46,58,"subtract"))

OPERATIONS = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b if b != 0 else exec('raise ValueError("Cannot divide by zero")'),
    "power": lambda a,b : a ** b,
    }
def calculator(*args, operation="add"):
    """Perform a calculation based on the operation."""
    if operation not in OPERATIONS:
        raise ValueError("Invalid operation")
    
    if len(args) < 2:
        raise ValueError("At least two numbers are required")
    result = args[0]
    for num in args[1:]:
        result = OPERATIONS[operation](result, num)
    return result

print("Output is:", calculator(5, 3, operation="add"))  # Output: 8
print("Output is:", calculator(10, 2, 3, operation="multiply"))  # Output: 60
print("Output is:", calculator(100, 20, operation="subtract"))  # Output: 80
print("Output is:", calculator(2, 3, operation="power"))  # Output: 8
print("Output is:", calculator(10, 5, operation="divide"))  # Output: 2.0

# 🚀 Supercharged Version
OPERATIONS = {
    "add": {
        "func": lambda *nums: sum(nums),
        "help": "Sum of all numbers"
    },
    "power": {
        "func": lambda a, b: a ** b,
        "help": "First number raised to power of second number"
    },
    "subtract": {
        "func": lambda a, b: a - b,
        "help": "Subtract second number from first"
    },
    "multiply": {
        "func": lambda *nums: eval('*'.join(map(str, nums))),
        "help": "Product of all numbers"
    },
    "divide": { 
        "func": lambda a, b: a/b if b != 0 else exec('raise ValueError("Cannot divide by zero")'),
        "help": "Divide first number by second"
        }
    # ... other operations ...
}

def calculator(*args, operation="add", show_help=False):
    """Advanced calculator with help system."""
    if operation == "help" or show_help:
        return "\n".join(f"{op}: {meta['help']}" for op, meta in OPERATIONS.items())
    
    if operation not in OPERATIONS:
        raise ValueError(f"Invalid operation. Try: {list(OPERATIONS.keys())}")
    
    try:
        return OPERATIONS[operation]["func"](*args)
    except TypeError as e:
        raise ValueError("Invalid arguments for operation") from e

# Now supports:
print(calculator(show_help=True))  # Shows operation list
print(calculator(2, 3, 4, operation="add"))  # Output: 9
# Problem 1:
x = 10  # Global variable

def foo():
    x = 20  # Local variable
    print("Inside foo():", x)

foo()
print("Outside foo():", x)
# Problem 2:
x = 10

def foo():
    global x  # Declare we're using the global x
    x = 20

foo()
print(x)

def outer():
    y = "outer"
    
    def inner():
        nonlocal y  # Refers to y in outer()
        y = "inner"
    
    inner()
    print(y)
# Problem 4:    
z = "global"

def test():
    z = "local"
    print(z)  # Which z does this print?

test()
print(z)
# Problem 1:
# Inside foo(): 20
# Outside foo(): 10                                                                                                                              
# Problem 2:                                                                                                                                                                       
# Output: 20                                                                                                                                                                              
# Problem 3:                                                                                                                                                                      
# Output: inner                                                                                                                                                                      
# Problem 4:
# local
# global
def make_counter():
    count = 0
    def counter():
        """A simple counter function that increments a count each time it's called."""      
    # Your task: Make count persist between calls
        nonlocal count
        count += 1
    return count 
  # Initialize the count attribute
counter = make_counter()
print(counter)

