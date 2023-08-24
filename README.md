# flask-api
This is a Flask API sample for getting stock info scraped from NASDAQ as of 2022/12/16.

Pre-requisition:
Python 3.9.17

## Start API
For the first time, please create an environment with the command below
```
poetry env use python
poetry shell
poetry install
```
After creating the environment, you can run the following at anytime
```
poetry shell
poetry run python run.py
```

## Sample post input json
```
{
    "stock_code":"TSLA"
}
```

## sample output json
```
{
    "industry": "Auto Manufacturing",
    "mkt_cap": 495135584003.0,
    "mkt_cap_gp": "mega",
    "sector": "Consumer Discretionary",
    "stk_code": "TSLA"
}
```
