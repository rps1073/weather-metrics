from utilities.extract_daily_forecast import extract_daily_forecast
from utilities.transform_daily_forecast import transform_daily_forecast
from utilities.load_daily_forecast import load_daily_forecast
from prefect import flow


@flow
def run_flow(conn, config):
    data = extract_daily_forecast(config)
    forecast_df_parsed = transform_daily_forecast(data)
    load_daily_forecast(conn, forecast_df_parsed)

    return
