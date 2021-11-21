start = 11
end = 30

"""
Python program to print all Prime numbers in an Interval

Input : start = 50 end = 100
Output : 53 59 61 67 71 73 79 83 89 97

Input : start = 900 end = 1000
Output : 907 911 919 929 937 941 947 953 967 971 977 983 991 997

"""

start =  int(input('Enter first number '))
end   = int(input('Enter end second number '))

for i in range(start, end+1):
    for j in range(2, i):
        if(i % j == 0):
            break
    else:
        print(i)