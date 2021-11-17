# how to add numbers in python using for loop
n = int(input('Enter the number '))
sum = 0

for num in range(0, n+1):
    sum = sum + num
print("SUM of first {0} numbers is {1}".format(n, sum))

# math formula 
n1 = int(input('Enter The number '))

sum_res = n1 * (n1 + 1) / 2

print('Sum of first {0} number is {1} '.format(n1, sum_res))