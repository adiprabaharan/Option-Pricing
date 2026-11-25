def test_parity():
    assert Call(strike, expiry) - Put(strike,expriy) == spot - strike * np.exp(-1 * rate * expiry)