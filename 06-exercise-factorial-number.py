"""
Python Program for factorial of a number
"""
# Recursive
def factorial(n):
    return 1 if(n == 1 or n == 0) else (n * factorial(n - 1))

num = 5

print('Factorial of {0} is {1} '.format(num, factorial(num)))

# factorial number
def factorial1(n1):
    if n1 < 0:
        return 0
    elif n1 == 0 or n1 == 1:
        return 1
    else:
        fact = 1
        while(n1 > 1):
            fact *= n1
            n1 -= 1
        return fact
num1 = 6
print('Factorial of {0} is {1} '.format(num1, factorial(num1)))

# By using In-built function
import math

def factorial2(n2):
    return math.factorial(n2)

num2 = 5
print('Factorial of {0} is {1} '.format(num2, factorial2(num2)))