"""
Program to print prime numbers from 1 to N.

Input: N = 10
Output: 2, 3, 5, 7

Input: N = 5
Output: 2, 3, 5 

"""

n = int(input('Enter the number '))

for i in range(1, n+1):
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        print(i)