# covid-metrics

### Create virtual env folder named "venv" in project directory
`virtualenv venv`

### Activate virtual env
`source venv/bin/activate`

### Install packages from requirements.txt
`pip install -r requirements.txt`

### Generate requirements.txt for brand new project
`pip freeze --local > requirements.txt`

### Install package in virtual env and add it to requirements.txt
`pip install psycopg2; pip freeze --local > requirements.txt`

### De-activate virtual env
`deactivate`

### Run app
`Python task.py`