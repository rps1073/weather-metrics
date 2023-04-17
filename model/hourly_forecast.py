import pandas as pd

def hourly_forecast(df):
    df_formatted = df[['time_epoch', 'time', 'temp_f', 'wind_mph', 'gust_mph']].rename(
        columns={
            'time_epoch': 'time_epoch',
            'time': 'timestamp',
            'temp_f': 'temp_f',
            'wind_mph': 'wind_mph',
            'gust_mph': 'gust_mph'
        })

    return df_formatted
