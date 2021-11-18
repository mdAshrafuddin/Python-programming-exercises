"""
Python program to find largest of n numbers
"""
def findMaximum(list):
    max = list[0]
    for m in list:
        if m > max:
            max = m
    return max

num = int(input('How many numbers: '))
lst = []

for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

print('Maximum element in the list is ', findMaximum(lst))

"""
Python program to find largest of n numbers using max
"""

list1 = []
num1 = int(input('How many numbers '))

for n1 in range(num1):
    numbers1 = int(input('Enter number '))
    list1.append(numbers1)

print("Maximum element in the list is :", max(list1))

