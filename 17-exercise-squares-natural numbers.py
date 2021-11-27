def sumSquare(n):
    sum = 0

    for i in range(n+1):
        sum = sum + (i * i)

    return sum

n = 4

print(sumSquare(n))

"""
Sum of squares of first N natural numbers = (N*(N+1)*(2*N+1))/6
"""

def cubeSquares(n):
    x = (n * (n + 1) * (2 * n + 1)) //6
    return x
x = int(input('Enter the Number '))
print(cubeSquares(x))

"""
For large n, the value of (n * (n + 1) * (2 * n + 1)) would overflow. 
We can avoid overflow up to some extent using the fact that n*(n+1) must be divisible by 2.
"""
def cubeSquares1(n):
    x = (n * (n+1) / 2) * (2 * n + 1) / 3
    return x

x = int(input('Enter the Number '))
print(cubeSquares1(x))