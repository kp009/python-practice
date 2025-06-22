# Write a function 'find_max(a,b,c)' that returns the largest of the 3 numbers
# find_max(4,9,2) -> 9
def find_max(a,b,c):
    if (a > b and a > c):
        return a
    elif (b > a and b > a):
        return b
    elif (c > a and c > b):
        return c

print(find_max(4, 9, 2))

# Write a function 'factorial(n)' that returns the factorial of the number n
# ex: factorial(5)-> 120
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = i*fact
    return fact

print(factorial(5))

# Create a function `greet(name="Guest")` that prints 'Hello, <name>'.
# Try calling it with and without passing a name.
def greet(name = "Guest"):
    return ( "Hello", name)

print(greet("python"))

# Write two versions of a function `multiply(a, b)`:
# - One that prints the result
# - One that returns the result
# Then show the difference in usage.
def multiply(a,b):
    return a*b

print(multiply(9,80))

def multiply(a,b):
    print(a*b)

multiply(9,80)

# Given: x = 10

# Write a function `change_x()` that sets x = 5 and prints it. Then print x outside the function.
# Observe how local vs global variables behave.
# Try again using the `global` keyword inside the function.
x = 10
def change_x():
   global x
   x = 5

change_x()
print(x)
