from constants.weather_api_sample_response import weather_api_sample_response
from utilities.transform_daily_forecast import transform_daily_forecast
import numpy


def test_transform_daily_forecast():
    df = transform_daily_forecast(weather_api_sample_response)
    forecast_date = df["FORECAST_DATE"]

    numpy.testing.assert_array_equal(forecast_date, "2022-05-01")
