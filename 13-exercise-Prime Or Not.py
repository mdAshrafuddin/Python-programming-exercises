"""
Python Program To Check Whether The Number Is Prime Or Not
"""

# number = int(input("Enter the number "))

# if number > 1:
#     for i in range(2, int(number) + 1):
#         if(number % i == 0):
#             print('Prime is not number ', i)
#             break
#     else:
#         print('Prime is number ')
# else:
#     print('Prime is not number ')



n = int(input('Enter the number '))

if n > 1:
    for i in range(2, n+1):
        if (n % i) == 0:
            print('It is not Prime number ')
            break
    else:
        print('It is Prime number ') 
# Enter the number is less than or equal 1
else:
    print('It is not Prime number ')  
    