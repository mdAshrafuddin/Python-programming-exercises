# how to add numbers in python using for loop
n = int(input('Enter the number '))
sum = 0

for num in range(0, n+1):
    sum = sum + num
print("SUM of first {0} numbers is {1}".format(n, sum) )