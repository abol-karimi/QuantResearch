import pandas as pd
from datetime import datetime

from binance.client import Client as bnb_client


client = bnb_client(tld='US')


def get_close(symbol, freq, start_ts, end_ts):
    data = client.get_historical_klines(symbol, freq, start_ts, end_ts)

    # convert the nested list to a dataframe
    columns = ['open_time','open','high','low','close','volume','close_time','quote_volume',
               'num_trades','taker_base_volume','taker_quote_volume','ignore']
    data = pd.DataFrame(data, columns=columns)

    # Convert from POSIX timestamp (number of millisecond since Jan 1, 1970)
    data['open_time'] = data['open_time'].map(lambda x: datetime.fromtimestamp(x/1000))
    data['close_time'] = data['close_time'].map(lambda x: datetime.fromtimestamp(x/1000))

    # Return the close-price series (indexed by open_time)
    return data.set_index('open_time')['close'].astype(float)
