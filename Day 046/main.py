import requests
from bs4 import BeautifulSoup
import lxml

# ranking_date = input('Enter the date in a "YYYY-MM-DD" format:')
ranking_date = '1982-12-14'

URL = 'https://www.billboard.com/charts/hot-100/'

response = requests.get(url=f'{URL}{ranking_date}/')

ranking_webpage = response.text
# print(ranking_webpage)
soup = BeautifulSoup(ranking_webpage, 'html.parser')

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)