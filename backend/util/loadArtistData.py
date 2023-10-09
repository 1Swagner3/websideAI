import json
from util.albumToText import json_to_text
from util.getSpotifyData import get_spotify_data


def load_artist_data():
    # Read biography
    with open("backend/artistData/biography.txt", "r") as file:
        biography = file.read()

    # Fetch Album Data from Spotify API
    album_data = get_spotify_data

    return {
        "biography": biography,
        "album_data": album_data,
        # ...
    }

def load_lyrics(song_title):
    with open(f"backend/artistData/lyrics/{song_title}.txt", "r") as file:
        lyrics = file.read()
    
    return lyrics

def load_album_data():
    album_data = get_spotify_data
    return album_data