import numpy as np
import pandas as pd


def strategy_returns(strategy, market_returns):
    """
    strategy: the long/short portfolio weights of each asset
    market_returns: the market return of each traded asset
    """
    portfolio = strategy.shift()
    returns_per_asset = portfolio * market_returns
    return returns_per_asset.sum(axis=1)


def volatility(returns, period):
    pass


def sharpe_ratio(returns, period, annualized=True):
    """period is in hours"""
    sr = returns.mean() / returns.std()
    if annualized:
       return sr * np.sqrt(252 * 24 / period)
    else:
        return sr


def max_drawdown(returns_cumulative):
    """Drawdown is either zero (no loss), or negative (loss as a ratio of the peak).
    Returns the maximum (in magnitude) drawdown"""
    running_max = returns_cumulative.expanding().max()
    running_drawdown = returns_cumulative / running_max - 1
    # return the minimum since drawdowns are nonpositive
    return running_drawdown.min()


def max_drawdown_stats(returns_cumulative):
    running_max = returns_cumulative.expanding().max()
    running_drawdown = returns_cumulative / running_max - 1
    # Find index of the maximum drawdown (in magnitude), and its value
    max_dd_idx = running_drawdown.idxmin()
    max_dd = running_drawdown.loc[max_dd_idx]

    # Find the index of the peak before the max drawdown
    last_peak_idx = running_max.loc[:max_dd_idx].idxmax()

    # Determine recovery (if any)
    peak_value = running_max.loc[last_peak_idx]
    recovery_mask = (returns_cumulative.loc[max_dd_idx:] >= peak_value)
    recovered = recovery_mask.any()

    if recovered:
        recovery_idx = recovery_mask.idxmax()
    else:
        recovery_idx = returns_cumulative.index[-1]

    return {
        'value': max_dd,
        'peak_date': last_peak_idx,
        'trough_date': max_dd_idx,
        'recovery_date': recovery_idx if recovered else None,
        'drawdown_series': running_drawdown,
    }
