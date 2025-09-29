

def rolling_avg_rank(ret, horizon):
    """
    Calculate a dollar-neutral portfolio by ranking the cross-section of momentum
    The momentum of each ticker is its rolling average of returns over the past horizon

    Args:
        ret (pd.DataFrame): time series of returns for each ticker
        horizon (int): number of trading periods to look back

    Returns:
        List(int): portfolio weights
    """
    # The momentum of each ticker: average returns in the past (up to the horizon)
    avg_ret = ret.rolling(horizon, min_periods=1).mean()
    # Rank cross-section of momentum
    ranks = avg_ret.rank(axis=1)
    # Dollar-neutralized ranks (mean zero)
    ranks = ranks.subtract(ranks.mean(axis=1), 0)
    # Scale the magnitudes so that the magnitudes add to 1
    weights = ranks.divide(ranks.abs().sum(axis=1), 0)
    return weights


