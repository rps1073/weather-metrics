import requests


def extract_daily_forecast(config):
    print("Querying API")
    url = f"https://api.weatherapi.com/v1/history.json?key={config['api_key']}&q={config['location']}&dt={config['start_date']}&end_dt={config['end_date']}"

    response = requests.request("GET", url, headers={}, data={})
    data = response.json()

    return data
