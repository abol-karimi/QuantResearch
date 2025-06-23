import pandas as pd

import quant.data.interface.binance as binance


def get_returns(tickers, freq, start_ts, end_ts, interface='binance'):
    if interface == 'binance':
        return get_returns_binance(tickers, freq, start_ts, end_ts)
    else:
        raise NotImplementedError(f'Interface {interface} is not implemented!')


def get_returns_binance(tickers, freq, start_ts, end_ts):
    prices = {x: binance.get_close(x, freq, start_ts=start_ts, end_ts=end_ts) for x in tickers}
    prices = pd.DataFrame.from_dict(prices, orient='columns')
    prices = prices.reindex(pd.date_range(prices.index[0], prices.index[-1], freq=freq))
    returns = prices.pct_change(fill_method=None)
    return returns
