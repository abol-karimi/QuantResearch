import numpy as np


def sharpe_ratio(returns, period, annualized=True):
    """period is in hours"""
    sr = returns.mean() / returns.std()
    if annualized:
       return sr * np.sqrt(252 * 24 / period)
    else:
        return sr