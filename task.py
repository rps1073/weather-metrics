import snowflake.connector
from constants.config import config
from utilities.extract_daily_forecast import extract_daily_forecast
from utilities.transform_daily_forecast import transform_daily_forecast
from utilities.load_daily_forecast import load_daily_forecast


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

    data = extract_daily_forecast(config)
    forecast_df_parsed = transform_daily_forecast(data)
    load_daily_forecast(conn, forecast_df_parsed)

    conn.close()

except Exception as e:
    print(e)

print("Task complete")
