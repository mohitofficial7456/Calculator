import sys
from functools import reduce

lst = []

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print("Please consider the below:-\n"
    " - for subtraction\n"
    " + for addition\n"
    " / for division\n"
    " * for multiplication")
operation = input("Please enter the operation you want to perform - ")

if(operation == "/"):
    a = int(input("please enter a - "))
    b = int(input("please enter b - "))
else:
    inp = input("Enter the values : ").split()
    lst = [int(i) for i in inp]

if(operation == "+"):
    s = reduce(add,lst)
    print(s)

elif(operation == "-"):
    s = reduce(sub,lst)
    print(s)

elif(operation == "/"):
    try:
        print(divide(a,b))
    except Exception as e:
        print(f"error! : {e}")
    else:
        print("Better Luck next time")
    finally:
        print("Good BYE")

elif(operation == "*"):
    s = reduce(multiply,lst)
    print(s)
    
else:
    print("Please enter a valid operation")
    