# Functions
# Chiune Honda
# 26 February 2024

# Create a Function called say_hello
# When you call it, it prints Hello!

def say_hello():
    print("Hello!")


# Create a function called say_hello_params
# The parameter we pass in is the name of the person that we're greeting
    
def say_hello_params(name):
    print(f"Hello {name.capitalize()}!")


# say_hello()
# say_hello_params("Jeffrey")
# say_hello_params("Thomas")
# say_hello_params("thomas")

# Create a function that takes a number and tells you how big that number is

def how_big(num):
    if num < 0:
        return "Very small"
    if num < 10:
        return "Prety small"
    if num < 100:
        return "Big"
    if num < 1000:
        return "Pretty big"
    return "Very big"

digit = int(input("type in number"))
print(how_big(digit))


#Create a function called adder
# Accept two inputs 
# Return the sum of the inputs

def adder(x: int, y: int) -> int:
    return x + y

result = adder(1, 1)
print(result)