# Add top 100 songs of a given year and date in you spotify as a new playlist

import os
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()


# Get Songs from BillBoard
def get_billboard_data():
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
    url = "https://www.billboard.com/charts/hot-100/" + date
    response = requests.get(url=url, headers=header)

    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_spans = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_names_spans]

    pprint(song_names)

    return song_names


# Prepare List of Songs for new playlist
def prepare_list_of_songs_for_playlist():
    song_uris = []
    counter = 1
    for song in get_billboard_data():
        song_name = song.strip()
        result = sp.search(q=song_name, type="track")
        print(counter)
        counter += 1
        if counter > 4:
            break

        if result["tracks"]["items"]:
            song_uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(song_uri)
        else:
            print(f"Song {song_name} not found on Spotify")

    return song_uris


# Create and Add a new playlist on Spotify
def create_and_and_new_playlist(songs_list):
    playlist_name = f"Billboard Hot 100 - {date}"
    description = "Top 100 songs on Billboard charts for the specified year."

    playlist = sp.user_playlist_create(user=sp.current_user()['id'],
                                       name=playlist_name,
                                       description=description,
                                       public=False)
    # Adding songs to playlist
    sp.playlist_add_items(playlist_id=playlist["id"], items=songs_list)


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# date = '2025-06-06'

scope = "playlist-read-private, " \
        "user-read-currently-playing, " \
        "user-read-currently-playing, " \
        "user-follow-read, playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    redirect_uri='http://127.0.0.1:8888/callback',
    scope=scope)
)

songs_to_add = prepare_list_of_songs_for_playlist()
create_and_and_new_playlist(songs_to_add)
