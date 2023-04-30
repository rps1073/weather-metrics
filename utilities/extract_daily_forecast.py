import requests
from prefect import task


@task(name="extract_daily_forecast_task")
def extract_daily_forecast(config):
    url = f"https://api.weatherapi.com/v1/history.json?key={config['api_key']}&q={config['location']}&dt={config['start_date']}&end_dt={config['end_date']}"

    response = requests.request("GET", url, headers={}, data={})
    data = response.json()

    return data
