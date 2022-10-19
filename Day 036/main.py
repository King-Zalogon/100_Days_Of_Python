# Stock Prices Monitor App
import requests
import datetime as dt

STOCK_KEY = "L2MAIFZDE50V79MU"


def yesterday_date():
    year = now.year
    month = now.month
    yesterday = now.day - 1

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
    else:
        pass

    return f"{year}-{month}-{yesterday}"


def two_days_ago_date():
    year = now.year
    month = now.month
    two_days_ago = now.day - 2

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
    else:
        pass

    return f"{year}-{month}-{two_days_ago}"

# TODO 1) Pull the Stock Price for Day N, the the price for N-1
# How mucho it increased or decreased, in amount and in percentage


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": STOCK_KEY
}

stock_daily_url = 'https://www.alphavantage.co/query'
r = requests.get(stock_daily_url, parameters)
data = r.json()

now = dt.datetime.now()
today = f"{now.year}-{now.month}-{now.day}"
yesterday = yesterday_date()
ereyesterday = two_days_ago_date()

closing_yesterday = float(data["Time Series (Daily)"][yesterday]['4. close'])
closing_ereyesterday = float(data["Time Series (Daily)"][ereyesterday]['4. close'])

balance = round(closing_yesterday-closing_ereyesterday, 4)
balance_percentage = f"{round((closing_yesterday-closing_ereyesterday)/closing_yesterday*100, 2)}%"
print(closing_yesterday)
print(closing_ereyesterday)
print(balance)
print(balance_percentage)




# TODO 2) Relevant New for that Stock's Company to understand the reason

# TODO 3) Send us SMS from Twilio with the facts to decide.
