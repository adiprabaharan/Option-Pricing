import numpy as np

def calc(p, prob, factor):

    if len(p) > 1:
        n=[]
        for i in range(len(p) - 1):
            n.append(factor * (prob * p[i] + (1 - prob) * p[i + 1]))
        j = n.copy()
        return calc(j, prob, factor)

    else:
        return p

class BinomialPricer:
    def __init__(self, m, c, N):
        self.m = m
        self.c = c
        self.step = N
        self.time = c.expiry / N
        self.u = np.exp(self.m.vol * np.sqrt(self.time))
        self.d = 1 / self.u
        self.prob = (np.exp(m.rate * self.time) - self.d) / (self.u - self.d)

    def pricer(self):
        initial = self.m.spot * self.u**self.step
        p = []

        factor = 1 / (np.exp(self.m.rate * self.time))

        for i in range(self.step + 1):
            p.append(initial * self.d**(2 * i))

        price = np.array(p)

        price = self.c.payoff(price)

        return calc(price, self.prob, factor)[0]