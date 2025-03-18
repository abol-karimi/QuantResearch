import pandas as pd
from binance.client import Client as bnb_client

client = bnb_client(tld='US')


def get_binance_px(symbol, freq, start_ts='2020-01-01', end_ts='2022-12-31'):
    data = client.get_historical_klines(symbol,freq,start_ts,end_ts)
    columns = ['open_time','open','high','low','close','volume','close_time','quote_volume',
               'num_trades','taker_base_volume','taker_quote_volume','ignore']

    data = pd.DataFrame(data,columns = columns)

    # Convert from POSIX timestamp (number of millisecond since Jan 1, 1970)
    data['open_time'] = data['open_time'].map(lambda x: datetime.fromtimestamp(x/1000))
    data['close_time'] = data['close_time'].map(lambda x: datetime.fromtimestamp(x/1000))
    return data
