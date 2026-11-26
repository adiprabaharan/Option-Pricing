import numpy as np
from scipy.stats import norm

from pricer.options import Call, Put

class BlackScholes():
    def __init__(self, m, c):
        #m is market
        #c is call
        self.option = c
        self.s0 = m.spot
        self.k = c.strike
        self.r = m.rate
        self.vol = m.vol
        self.t = c.expiry
        self.d1 = (np.log(self.s0 / self.k) + (self.r + 0.5*self.vol**2)*self.t) / (self.vol*np.sqrt(self.t))
        self.d2 = self.d1 - self.vol*np.sqrt(self.t)

    def pricer(self):
        call_price = self.s0 * norm.cdf(self.d1) - self.k * np.exp(-1 * self.r * self.t) * norm.cdf(self.d2)
        put_price = call_price - self.s0 + self.k*np.exp(-1 * self.r *self.t)
        
        if isinstance(self.option, Call):
            return call_price
        else:
            return put_price