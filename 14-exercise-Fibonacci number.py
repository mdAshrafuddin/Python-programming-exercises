# Python Program for n-th Fibonacci number

def fibonacci(n):
    a = 0
    b = 1

    if n < 0:
       print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b  # 0 + 1  = 1 1 + 1 = 2 2 + 1 =3 
            a = b
            b = c
        return b

n = input('Enter the number ')
n = int(n)

for i in range(0, n+1):
    print(fibonacci(i))

# ( Use recursion ) 
print('\n')
def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n -1) + Fibonacci(n -2)

print(Fibonacci(10))