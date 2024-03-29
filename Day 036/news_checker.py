import os
import requests as rq
from fluctuation_check import yesterday_date as yd
from fluctuation_check import two_days_ago_date as eyd
from dotenv import load_dotenv

load_dotenv()


NEWS_API = os.getenv('NEWS_KEY')
NEWS_URL = "https://newsapi.org/v2/everything"


def news_checker(symbol):
    parameters = {
        "apiKey": NEWS_API,
        "q": symbol,
        "searchIn": ["title", "content"],
        "from": eyd(),
        "to": yd(),
        "sortBy": "relevancy",
        "pageSize": 10

    }

    response = rq.get(NEWS_URL, params=parameters)
    news_data = response.json()

    top_news = []
    for n in range(len(news_data['articles'])):
        top_news.append(news_data['articles'][n]['title'])

    return top_news
