from utilities.run_flow import run_flow
from constants.config import config
import snowflake.connector


print("Starting task")

try:
    print("Connecting to db")
    conn = snowflake.connector.connect(
        user=config["snowflake_user"],
        password=config["snowflake_pw"],
        account=config["snowflake_account"],
        warehouse=config["snowflake_warehouse"],
        database=config["snowflake_database"],
        schema=config["snowflake_schema"],
    )

    run_flow(conn, config)

    conn.close()

except Exception as e:
    print(e)

print("Task complete")
