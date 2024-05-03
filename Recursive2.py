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
    if not n % 2 == 0:
        return n + sumoddN(n-1)
    else:
        return sumoddN(n-1)
print(sumoddN(4))


#wap a recursive function to calculate sum of first N eve natural numbers
def sumevenN(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return n + sumevenN(n-1)
    else:
        return sumevenN(n-1)    
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
print(sumsquareN(3))