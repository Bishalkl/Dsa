# Simple example of Recursive concept of function
#Example
def sum(n):
    if n == 1:
        return 1
    s = n + sum(n-1)
    return s

a = sum(4)
print(a)

#Basic stuff should we know to make Recursive function
#Recursive case
#Base case



