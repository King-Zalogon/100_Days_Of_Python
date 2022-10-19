# Stock Prices Monitor App
import requests as rq
import datetime as dt
import pandas as pd
import fluctuation_check as fc
from news_checker import news_checker

csv = pd.read_csv("stock_symbols.csv", sep='|')
symbols = csv.to_dict(orient="records")
symbols_list = [symbols[n]["Symbol"] for n in range(len(symbols))]

# TODO 1) Pull the Stock Price for Day N, the the price for N-1
# How mucho it increased or decreased, in amount and in percentage

today_movements = []
for company in symbols_list:
    today_movements.append(fc.fluctuation_check(company))

most_fluctuation = ()
fluctuation = 0.0

for n in range(5):
    if abs(today_movements[n][2]) > fluctuation:
        fluctuation = abs(today_movements[n][2])
        most_fluctuation = today_movements[n]
    else:
        pass


# TODO 2) Relevant New for that Stock's Company to understand the reason

top_company = ''
for n in range(5):
    if most_fluctuation[0] in symbols[n].values():
        top_company = symbols[n]['Company Name'].split()[0].split(".")[0]

top_news = news_checker(top_company)

print(top_news)

# TODO 3) Send us SMS from Twilio with the facts to decide.

