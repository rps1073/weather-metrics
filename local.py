from utilities.run_flow import run_flow
from constants.config import config

try:
    run_flow(config)

except Exception as e:
    print(e)
