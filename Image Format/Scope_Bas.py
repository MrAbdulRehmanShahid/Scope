
x = 10  # Global variable

def foo():
    x = 20  # Local variable
    print("Inside foo():", x)

foo()
print("Outside foo():", x)

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
    outer()
    print(y)    
z = "global"

def test():
    z = "local"
    print(z)  # Which z does this print?
test()
print(z)

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

def make_multipler(factor):
    call_count = 0
    def multipler(x):
        nonlocal call_count
        call_count +=1
        print(f"Call count: {call_count}")  
        return x * factor
    return multipler
triple = make_multipler(3)
print(triple(5)) #  Output: 15  

temp = 5
cel = 0
fahr = float(temp)
cel = (fahr - 32.0) * 5.0/9.0
print(cel) 