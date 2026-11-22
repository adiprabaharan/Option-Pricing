import numpy as np

class Option:
    def __init__(self, strike, expiry):
        self.strike = strike
        self.expiry = expiry

    def payoff(self, S):
        raise NotImplementedError

class Call(Option):
    def payoff(self, S):
        return np.maximum(S - self.strike, 0)


class Put(Option):
    def payoff(self, S):
        return np.maximum(self.strike - S, 0)
