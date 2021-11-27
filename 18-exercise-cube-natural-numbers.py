"""
Python Program for cube sum of first n natural numbers

Print the sum of series 13 + 23 + 33 + 43 + …….+ n3 till n-th term.
"""
import math

def sumOfSeries(n):
    sum = 0

    for i in range(n+1):
        sum = sum + i * i * i
    return sum

n = 4

print(sumOfSeries(n))


# An efficient solution is to use direct mathematical formula which is (n ( n + 1 ) / 2) ^ 2
def cubeSeries(n):
    x = (n * (n+1)//2) ** 2

    return x 

n = int(input("Enter the number "))

print('The Cube number ', cubeSeries(n))