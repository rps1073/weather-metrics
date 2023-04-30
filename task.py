import requests
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from model.parse_daily_forecast import parse_daily_forecast
from constants.config import config


print("Starting task")

try:
    print("Connecting to db")
    conn = snowflake.connector.connect(
        user=config["snowflake_user"],
        password=config["snowflake_pw"],
        account=config["snowflake_account"],
        warehouse=config["snowflake_warehouse"],
        database=config["snowflake_database"],
        schema=config["snowflake_schema"],
    )

    url = f"https://api.weatherapi.com/v1/history.json?key={config['api_key']}&q={config['location']}&dt={config['start_date']}&end_dt={config['end_date']}"

    print("Querying API")
    response = requests.request("GET", url, headers={}, data={})
    data = response.json()

    forecast_df_parsed = parse_daily_forecast(data)

    print("Writing to db")
    write_pandas(conn, forecast_df_parsed, "DAILY_FORECAST")

    conn.close()

except Exception as e:
    print(e)

print("Task complete")
