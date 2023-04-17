import pandas as pd

def parse_daily_forecast(df, location_series):
    df_formatted = df[['date']].rename(
        columns={
            'date': 'forecast_date',
        })
    
    day_dict = df['day']

    df_formatted['mintemp_f'] = pd.Series([key['mintemp_f'] for key in day_dict])    
    df_formatted['maxtemp_f'] = pd.Series([key['maxtemp_f'] for key in day_dict])
    df_formatted['avgtemp_f'] = pd.Series([key['avgtemp_f'] for key in day_dict])
    df_formatted['maxwind_mph'] = pd.Series([key['maxwind_mph'] for key in day_dict])
    df_formatted['totalprecip_in'] = pd.Series([key['totalprecip_in'] for key in day_dict])
    df_formatted['avghumidity'] = pd.Series([key['avghumidity'] for key in day_dict])

    astro_dict = df['astro']

    df_formatted['sunrise'] = pd.Series([key['sunrise'] for key in astro_dict])
    df_formatted['sunset'] = pd.Series([key['sunset'] for key in astro_dict])
    df_formatted['moonrise'] = pd.Series([key['moonrise'] for key in astro_dict])
    df_formatted['moonset'] = pd.Series([key['moonset'] for key in astro_dict])
    df_formatted['moon_phase'] = pd.Series([key['moon_phase'] for key in astro_dict])
    df_formatted['moon_illumination'] = pd.Series([key['moon_illumination'] for key in astro_dict])

    df_formatted['city'] =  pd.Series([location_series['name'] for x in range(len(df.index))])
    df_formatted['state'] =  pd.Series([location_series['region'] for x in range(len(df.index))])

    return df_formatted
