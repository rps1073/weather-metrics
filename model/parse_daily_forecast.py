import pandas as pd

def parse_daily_forecast(df, location_series):
    df_formatted = df[['date']].rename(
        columns={
            'date': 'FORECAST_DATE',
        })
    
    day_dict = df['day']

    df_formatted['MINTEMP_F'] = pd.Series([key['mintemp_f'] for key in day_dict])    
    df_formatted['MAXTEMP_F'] = pd.Series([key['maxtemp_f'] for key in day_dict])
    df_formatted['AVGTEMP_F'] = pd.Series([key['avgtemp_f'] for key in day_dict])
    df_formatted['MAXWIND_MPH'] = pd.Series([key['maxwind_mph'] for key in day_dict])
    df_formatted['TOTALPRECIP_IN'] = pd.Series([key['totalprecip_in'] for key in day_dict])
    df_formatted['AVGHUMIDITY'] = pd.Series([key['avghumidity'] for key in day_dict])

    astro_dict = df['astro']

    df_formatted['SUNRISE'] = pd.Series([key['sunrise'] for key in astro_dict])
    df_formatted['SUNSET'] = pd.Series([key['sunset'] for key in astro_dict])
    df_formatted['MOON_PHASE'] = pd.Series([key['moon_phase'] for key in astro_dict])

    df_formatted['CITY'] =  pd.Series([location_series['name'] for x in range(len(df.index))])
    df_formatted['STATE'] =  pd.Series([location_series['region'] for x in range(len(df.index))])

    return df_formatted
