import pandas as pd

import quant.data.interface.binance as binance


def download_returns(tickers, freq, start_ts, end_ts, interface='binance'):
    if interface == 'binance':
        data = {x: binance.get_returns(x, freq, start_ts=start_ts, end_ts=end_ts) for x in tickers}
        return pd.DataFrame(data)
    else:
        raise NotImplementedError(f'Interface {interface} is not implemented!')
