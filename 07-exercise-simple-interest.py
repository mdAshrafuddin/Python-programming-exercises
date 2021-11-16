"""
Python Program for simple interest
"""
def simple_interest(p, t, r):
    print('The principle is ', p)
    print('The time period is ', t)
    print('The rate is ', r)

    si = (p * t * r) / 100
    print('The simple interest is ', si)
    return si

simple_interest(3, 4, 15)
