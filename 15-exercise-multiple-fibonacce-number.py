# Python Program for n\’th multiple of a number in Fibonacci Series

def mulFibo(k, n):
    a = 0
    b = 1
    i = 2
    while i != 0:
        c = a + b
        a = b
        b = c

        if b % k == 0:
            return n * i
        
        i +=1
    return 
    
n = 5

k = 4

print(mulFibo(k, n))
