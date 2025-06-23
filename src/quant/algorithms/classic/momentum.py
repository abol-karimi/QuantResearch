

def rolling_avg_rank(ret, horizon):
    """
    Input data: returns of each ticker over a fixed past horizon
    Data statistics (functions of data): average returns of each ticker over the horizon
    Long-short signal (ticker weight): demeaned rank ratio of each ticker statistic

    This is a variation of the UMD (Up-Minus-Down) strategy
    """
    # At each period, rank the stocks based on their average return over the past horizon
    avg_ret_rank = ret.rolling(horizon, min_periods=1).mean().rank(axis=1)
    # Subtract the ranks by their mean to neutralize our strategy to the ticker with average rank
    avg_ret_rank = avg_ret_rank.subtract(avg_ret_rank.mean(axis=1), 0)
    # Normalize the ranks by their average so that they represent the weights of our portfolio
    weights = avg_ret_rank.divide(avg_ret_rank.abs().sum(axis=1), 0)
    return weights


