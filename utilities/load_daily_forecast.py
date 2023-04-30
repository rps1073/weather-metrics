from snowflake.connector.pandas_tools import write_pandas

def load_daily_forecast(conn, forecast_df_parsed):
    print("Writing to db")
    write_pandas(conn, forecast_df_parsed, "DAILY_FORECAST")

    return