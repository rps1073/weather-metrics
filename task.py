import psycopg2
import pandas as pd
import os
from decouple import config
from sqlalchemy import create_engine

print('Starting task')
db_config = {
    "user": config('username'),
    "password": config('password'),
    "host": config('host'),
    "database": config('database'),
}

try:
    conn_string = f'postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}/{db_config["database"]}'
    db = create_engine(conn_string)
    conn = db.connect()

    data = pd.read_sql('SELECT * FROM covid_metrics_raw.daily_cases_average LIMIT 1;', conn)
    print(data)
    
    conn.close()
except Exception as e:
    print(e)

print('Task complete')