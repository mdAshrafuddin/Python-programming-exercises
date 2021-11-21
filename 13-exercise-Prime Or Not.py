"""
Python Program To Check Whether The Number Is Prime Or Not
"""

number = int(input("Enter the number "))

if number > 1:
    for i in range(2, int(number / 2) + 1):
        if(number % i == 0):
            print('Prime is not number ', i)
            break
    else:
        print('Prime is number ')
else:
    print('Prime is not number ', number)