import numpy as np
import pytest

from pricer.options import Call, Put
from pricer.market import Market
from pricer.BinomialPricer import BinomialPricer
def test_parity():
    m = Market(spot=100, rate=0.05, vol=0.2)
    c = Call(strike=100, expiry=1)
    p = Put(strike=100, expiry=1)
    assert BinomialPricer(m, c, 50).pricer() - BinomialPricer(m, p, 50).pricer() == pytest.approx(m.spot - c.strike * np.exp(-1 * m.rate * c.expiry))