#!/bin/env python3

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mult(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    
    return a / b

def pow(a, b):
    return a ** b

if __name__ == "__main__":
    print("Add: ", add(2,3))
    print("Sub: ", subtract(2,3))
    print("Mult: ", mult(2,3))
    print("Divide: ", divide(10, 2))
    print("Power: ", pow(5, 4))

