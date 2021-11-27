"""
Python Program for compound interest

Formula to calculate compound interest annually is given by: 
A = P(1 + R/100) t 
Compound Interest = A – P 
Where, 
A is amount 
P is principle amount 
R is the rate and 
T is the time span

"""

def compound_interest(principle, rate, time):
    total_amount = principle * (pow((1 + rate/100), time))
    ci = total_amount - principle
    print(ci)

principle = int(input('Enter the principle amount '))
rate = int(input('Enter the rate of interest '))
time = int(input('Enter the numbr of years '))

compound_interest(principle, rate, time)


p = 1000
r = 100
t = 2

com = p * (pow((1 + r / 100), t))

print(com)