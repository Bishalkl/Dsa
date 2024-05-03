#Assignment-19: simple problem on recursion

#Wap a recursive function to calculate sum of first N natural numbers.
def sumN(n):
    if n == 1:
        return 1
    sum = n + sumN(n-1)
    return sum

print(sumN(4))
print()

#Wap a recursive functionn to calculate sum of first N odd natural numbers
def sumoddN(n):
    if n == 1:
        return 1
    return 2*n-1 + sumoddN(n-1)
print(sumoddN(10))

#wap a recursive function to calculate sum of first N eve natural numbers
def sumevenN(n):
    if n == 1:
        return 2
    return 2*n + sumevenN(n-1) 
print(sumevenN(4))

#wap a recursive function to calculate a factorial of number.
def factorialN(n):
    if n == 1:
        return 1
    return n * factorialN(n-1)
print(factorialN(3))

#Wap a recursive function to calcuate sum of square of first N natural number
def sumsquareN(n):
    if n == 1:
        return 1
    return  (n ** 2 ) + sumsquareN(n - 1)
print(sumsquareN(5))