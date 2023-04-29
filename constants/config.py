import os
from dotenv import load_dotenv

load_dotenv(".env")

config = {
    "snowflake_user": os.environ["snowflake_user"],
    "snowflake_pw": os.environ["snowflake_pw"],
    "snowflake_account": os.environ["snowflake_account"],
    "snowflake_warehouse": os.environ["snowflake_warehouse"],
    "snowflake_database": os.environ["snowflake_database"],
    "snowflake_schema": os.environ["snowflake_schema"],
    "api_key": os.environ["api_key"],
    "location": os.environ["location"],
    "start_date": os.environ["start_date"],
    "end_date": os.environ["end_date"],
}
