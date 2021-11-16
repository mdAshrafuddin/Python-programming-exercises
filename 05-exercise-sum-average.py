"""
Python Find/Calculate the Sum and Average of n natural numbers using loop and range function
"""
n = int(input('Enter the number '))
sum = 0

for i in range(0, n+1):
    sum = sum  + i
average = sum / n

print("Sum of {0} number is {1} ".format(n, sum))
print("Sum of {0} average is {1} ".format(sum, average))