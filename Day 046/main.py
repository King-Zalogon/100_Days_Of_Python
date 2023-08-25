import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('ID')
CLIENT_SECRET = os.getenv('SECRET')


# ranking_date = input('Enter the date in a "YYYY-MM-DD" format:')
ranking_date = '1982-12-14'

URL = 'https://www.billboard.com/charts/hot-100/'
REDIRECT_URI = os.getenv('REDIRECT')

response = requests.get(url=f'{URL}{ranking_date}/')

ranking_webpage = response.text
# print(ranking_webpage)
soup = BeautifulSoup(ranking_webpage, 'html.parser')

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

song_authors_spans = soup.select(selector='li ul li span',
                                 class_="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max "
                                        "u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block "
                                        "a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")
song_authors = [author.getText().strip() for author in song_authors_spans]
song_authors = [author for author in song_authors if len(author) > 2]

# Now to use the Spotify API

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])