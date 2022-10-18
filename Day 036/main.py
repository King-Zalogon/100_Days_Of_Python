# Stock Prices Monitor App
import requests

STOCK_KEY = "L2MAIFZDE50V79MU"

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

print(data)


# TODO 2) Relevant New for that Stock's Company to understand the reason

# TODO 3) Send us SMS from Twilio with the facts to decide.
