import os
import requests
import datetime as dt
from dotenv import load_dotenv

load_dotenv()

STOCK_KEY = os.getenv('ALPHA_KEY')
STOCK_DAILY_URL = 'https://www.alphavantage.co/query'


def yesterday_date():
    year = dt.datetime.now().year
    month = dt.datetime.now().month
    yesterday = dt.datetime.now().day - 1

    if yesterday == 0:

        if month == 1:
            year -= 1
            month = 12

        else:
            month -= 1

        if month in [1, 3, 5, 7, 8, 10, 12]:
            yesterday = 31
        elif month == 2:
            yesterday = 28
        else:
            yesterday = 30
    elif yesterday < 10:
        yesterday = f'0{yesterday}'

    else:
        pass

    if month < 10:
        month = f'0{month}'

    else:
        pass

    return f"{year}-{month}-{yesterday}"


def two_days_ago_date():
    year = dt.datetime.now().year
    month = dt.datetime.now().month
    two_days_ago = dt.datetime.now().day - 2

    if two_days_ago == 0:

        if month == 1:
            year -= 1
            month = 12

        else:
            month -= 1

        if month in [1, 3, 5, 7, 8, 10, 12]:
            two_days_ago = 31
        elif month == 2:
            two_days_ago = 28
        else:
            two_days_ago = 30

    elif two_days_ago < 10:
        two_days_ago = f'0{two_days_ago}'

    else:
        pass

    if month < 10:
        month = f'0{month}'

    else:
        pass

    return f"{year}-{month}-{two_days_ago}"


def fluctuation_check(symbol: str):

    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": STOCK_KEY
    }

    r = requests.get(STOCK_DAILY_URL, parameters)
    stock_data = r.json()
    yesterday = yesterday_date()
    ereyesterday = two_days_ago_date()

    closing_yesterday = float(stock_data["Time Series (Daily)"][yesterday]['4. close'])
    closing_ereyesterday = float(stock_data["Time Series (Daily)"][ereyesterday]['4. close'])

    balance = round(closing_yesterday - closing_ereyesterday, 4)
    balance_percentage = round((closing_yesterday - closing_ereyesterday) / closing_yesterday * 100, 2)

    return symbol, balance, balance_percentage


