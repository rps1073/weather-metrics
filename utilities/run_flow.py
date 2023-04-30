from utilities.extract_daily_forecast import extract_daily_forecast
from utilities.transform_daily_forecast import transform_daily_forecast
from utilities.load_daily_forecast import load_daily_forecast
from prefect import flow
from prefect.task_runners import SequentialTaskRunner
import snowflake.connector


@flow(
    name="weather_metrics_flow",
    description="Runs ETL tasks to extract weather API data and push to a db",
    task_runner=SequentialTaskRunner(),
    log_prints=True,
)
def run_flow(config):
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

    return
