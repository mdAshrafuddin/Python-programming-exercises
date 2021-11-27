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

class Priciples:
    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t

    def show(self):
        si = (self.p * self.r * self.t) / 100
        print(si)

si = Priciples(8, 6, 8)

si.show()

