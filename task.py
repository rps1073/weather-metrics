import psycopg2
import pandas as pd
import json
import requests
from decouple import config
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from model.hourly_forecast import hourly_forecast

print('Starting task')
app_config = {
    "user": config('username'),
    "password": config('password'),
    "host": config('host'),
    "database": config('database'),
    "api_key": config('api_key'),
}

try:
    yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
    print(f"Weather Date: {yesterday}")
    url = f"https://api.weatherapi.com/v1/history.json?key={app_config['api_key']}&q=Somerville&dt={yesterday}"

    response = requests.request("GET", url, headers={}, data={})
    data = response.json()
    day_forecast = data['forecast']['forecastday'][0]['hour']
    forecast_df = pd.DataFrame(day_forecast)
    forecast_df_formatted = hourly_forecast(forecast_df)
    print(forecast_df_formatted)

except Exception as e:
    print(e)

print('Task complete')