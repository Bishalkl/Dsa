# Simple example of Recursive concept of function
#Example
def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)


a = sum(20)
print(a)

#Basic stuff should we know to make Recursive function
#Recursive case
#Base case


#Five first basic warm up example 

#First example 

#Wap a recursive function to print first N natural number
def printN(n):
    if n >= 1:
        printN(n-1)
        print(n, end=" ")

printN(12)
print()

#Second example 
#Wap a recursive function to print first N nautral number 
def printrevN(n):
    if n >= 1:
        print(n, end=" ")
        printrevN(n-1)

printrevN(12)
print()


#Third example 
#Wap a recursive function to print first N odd natural number
def printoddN(n):
    if n >= 1:
        printoddN(n-1)
        if not n % 2 == 0:
            print(n, end=" ")

printoddN(12)
print()

#Wap a recursive function to print first N even natural number
def printevenN(n):
    if n >= 1:
        printevenN(n - 1)
        if n % 2 is 0:
            print(n, end=" ")

printevenN(12)
print()


#Wap a recursive function to print first N odd natural number in reverse order
def printoddN(n):
    if n >= 1:
        if not n % 2 == 0:
            print(n, end=" ")
        printoddN(n-1)

printoddN(12)
print()

#Wap a recursive function to print first N even natural number in reverse order
def printevenN(n):
    if n >= 1:
        if n % 2 is 0:
            print(n, end=" ")
        printevenN(n - 1)

printevenN(12)
print()

