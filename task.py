import psycopg2
import pandas as pd
import json
import requests
from decouple import config
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from model.parse_daily_forecast import parse_daily_forecast

print('Starting task')
app_config = {
    "user": config('username'),
    "password": config('password'),
    "host": config('host'),
    "database": config('database'),
    "api_key": config('api_key'),
    "location": config('location'),
    "start_date": config('start_date'),
    "end_date": config('end_date'),
}

try:
    url = f"https://api.weatherapi.com/v1/history.json?key={app_config['api_key']}&q={app_config['location']}&dt={app_config['start_date']}&end_dt={app_config['end_date']}"
    print(url)

    conn_string = f'postgresql://{app_config["user"]}:{app_config["password"]}@{app_config["host"]}/{app_config["database"]}'
    read_db = create_engine(conn_string)
    read_conn = read_db.connect()

    table_history_df = pd.read_sql('SELECT * FROM weather_metrics_raw.daily_forecast;', read_conn)
    read_conn.close()

    response = requests.request("GET", url, headers={}, data={})
    data = response.json()
    
    location_data = data['location']
    location_series = pd.Series(location_data)

    day_forecast = data['forecast']['forecastday']
    forecast_df = pd.DataFrame(day_forecast)
    forecast_df_formatted = parse_daily_forecast(forecast_df, location_series)

    final_insert_df = pd.merge(
        table_history_df,
        forecast_df_formatted,
        how="outer",
    )

    print(final_insert_df)

    write_db = create_engine(conn_string)
    write_conn = write_db.connect()
    final_insert_df.to_sql('daily_forecast', write_conn, schema='weather_metrics_raw', if_exists='replace', index=False)

    write_conn.close()

except Exception as e:
    print(e)

print('Task complete')