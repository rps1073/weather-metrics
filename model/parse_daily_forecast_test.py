from parse_daily_forecast import parse_daily_forecast
import pandas as pd

def test_parse_daily_forecast():
    df = pd.DataFrame()
    location_series = pd.Series()
    print(df)
    assert parse_daily_forecast(df, location_series) == 4