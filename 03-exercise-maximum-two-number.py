"""
Maximum of two numbers in Python

Input: a = 2, b = 4
Output: 4

Input: a = -1, b = -4
Output: -1

"""
def maximum(a, b):
    if a >= b:
        return a
    else:
        return b

print(maximum(3, 5))


"""
Method #2: Using max() function
"""

a = 2
b = 4

maximum = max(a, b)

print(maximum)

"""
Method #3: useing ternary operator
"""

n = 42
m = 4

print(n if n >= m else m)

