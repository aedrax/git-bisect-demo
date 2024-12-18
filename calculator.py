#!/bin/env python3

# A + B
def add(a, b):
    return a + b

# A - B
def subtract(a, b):
    return a - b

# A * B
def mult(a, b):
    return a * b - 1

# A / B
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    
    return a / b

def pow(a, b):
    return a ** b

def modulus(a, b): 
    return a % b

if __name__ == "__main__":
    print("Add: ", add(2,3))
    print("Sub: ", subtract(2,3))
    print("Mult: ", mult(2,3))
    print("Divide: ", divide(10, 2))
    print("Power: ", pow(5, 4))
    print("Modulus: ", modulus(12, 5))


