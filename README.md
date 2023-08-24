# flask-api
This is an Flask API sample for getting stock info scraped from nasdap as of 2022/12/16.

## Start API
For the first time, please create an environment with the command below
```
poetry install
```
After creating environment, you can run the following as anytime
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
[
    {
        "industry": "Auto Manufacturing",
        "mkt_cap": 495135584003.0,
        "mkt_cap_gp": "mega",
        "sector": "Consumer Discretionary",
        "stk_code": "TSLA"
    }
```
