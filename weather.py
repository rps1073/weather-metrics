from dotenv import load_dotenv
import os
import requests
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from model.parse_daily_forecast import parse_daily_forecast

print('Starting task')
load_dotenv('.env')

config = {
    'snowflake_user': os.environ['snowflake_user'],
    'snowflake_pw': os.environ['snowflake_pw'],
    'snowflake_account': os.environ['snowflake_account'],
    'snowflake_warehouse': os.environ['snowflake_warehouse'],
    'snowflake_database': os.environ['snowflake_database'],
    'snowflake_schema': os.environ['snowflake_schema'],
    'api_key': os.environ['api_key'],
    'location': os.environ['location'],
    'start_date': os.environ['start_date'],
    'end_date': os.environ['end_date'],
}

try:
    print('Connecting to db')
    conn = snowflake.connector.connect(
        user=config['snowflake_user'],
        password=config['snowflake_pw'],
        account=config['snowflake_account'],
        warehouse=config['snowflake_warehouse'],
        database=config['snowflake_database'],
        schema=config['snowflake_schema'],
    )

    url = f"https://api.weatherapi.com/v1/history.json?key={config['api_key']}&q={config['location']}&dt={config['start_date']}&end_dt={config['end_date']}"

    print('Querying API')
    response = requests.request("GET", url, headers={}, data={})
    data = response.json()
    
    location_data = data['location']
    location_series = pd.Series(location_data)

    day_forecast = data['forecast']['forecastday']
    forecast_df = pd.DataFrame(day_forecast)
    forecast_df_parsed = parse_daily_forecast(forecast_df, location_series)

    print('Writing to db')
    write_pandas(conn, forecast_df_parsed, 'DAILY_FORECAST')

    conn.close()

except Exception as e:
    print(e)

print('Task complete')