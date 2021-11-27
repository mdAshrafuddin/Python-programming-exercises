# Python Program for n\’th multiple of a number in Fibonacci Series

def mulFibo(k, n):
    a = 0
    b = 1
    i = 2
    while i != 0:
        c = a + b
        a = b
        b = c
        # print(b)
        if b % k == 0:
            return n * i
        
        i +=1
        print(i)
    return 
  
n = 9

k = 6

print(mulFibo(k, n))
