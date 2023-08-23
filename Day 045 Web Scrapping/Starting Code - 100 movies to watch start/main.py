import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)

movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, 'html.parser')

movies = soup.find_all('h3', class_="listicleItem_listicle-item__title__hW_Kn")

movies_list = []

for movie in movies:
    movies_list.append(movie.text)

movies_list.reverse()

with open('movies.txt', 'w', encoding='UTF-8') as file:
    for movie in movies_list:
        file.write(f'{movie}\n')

with open('movies.txt', 'r', encoding='UTF-8') as file:
    print(file.read())
