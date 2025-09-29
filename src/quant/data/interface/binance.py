import pandas as pd
from datetime import datetime

from binance.client import Client as bnb_client


client = bnb_client(tld='US')


def get_returns(symbol, freq, start_ts, end_ts):
    # Each kline is a data row e.g.
    # [
    #     1499040000000,  # Open time
    #     "0.01634790",  # Open
    #     "0.80000000",  # High
    #     "0.01575800",  # Low
    #     "0.01577100",  # Close
    #     "148976.11427815",  # Volume
    #     1499644799999,  # Close time
    #     "2434.19055334",  # Quote asset volume
    #     308,  # Number of trades
    #     "1756.87402397",  # Taker buy base asset volume
    #     "28.46694368",  # Taker buy quote asset volume
    #     "17928899.62484339"  # Can be ignored
    # ]
    klines = client.get_historical_klines(symbol, freq, start_ts, end_ts)

    open_time = [datetime.fromtimestamp(row[0]/1000) for row in klines] # Convert POSIX timestamps to datatime objects
    close = [float(row[4]) for row in klines]
    ret = pd.Series(close, index=open_time).pct_change(fill_method=None)
    ret.index.name = 'open-time'
    return ret
