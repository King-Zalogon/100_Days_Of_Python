import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

item_url = 'https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B099VMT8VZ/'

my_headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept-Language':
    'en-US,en;q=0.5',
}

response = requests.get(url=item_url, headers=my_headers)
# print(response)
item_webpage = response.text
# print(item_webpage)
soup = BeautifulSoup(item_webpage, 'lxml')
