from snowflake.connector.pandas_tools import write_pandas
from prefect import task


@task(name="load_daily_forecast_task")
def load_daily_forecast(conn, forecast_df_parsed):
    write_pandas(conn, forecast_df_parsed, "DAILY_FORECAST")

    return
