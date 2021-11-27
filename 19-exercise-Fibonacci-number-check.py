# Python Program for How to check if a given number is Fibonacci number?

n = int(input("Enter the number: "))
c = 0
a = 1
b = 1
if n == 0 or n == 1:
   print("Yes")
else :
   while c < n:
        c = a + b
        b = a
        a = c
if c == n:
   print(n, " is Fibonacci number")
else :
   print(n, " is not Fibnacci number")