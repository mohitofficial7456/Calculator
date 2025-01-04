# simple calculator

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

a = int(input("please enter a - "))
b = int(input("please enter b - "))
print("Please consider the below:-\n"
" - for subtraction\n"
" + for addition\n"
" / for division\n"
" * for multiplication")
operation = input("Please enter the operation you want to perform - ")

if(operation == "+"):
    print(add(a,b))
elif(operation == "-"):
    print(sub(a,b))
elif(operation == "/"):
    print(divide(a,b))
elif(operation == "*"):
    print(multiply(a,b))
else:
    print("Please enter a valid operation")
    