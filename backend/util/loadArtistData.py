
from util.getSpotifyData import get_spotify_data
from chatBots.getSongInfo import get_song_info


def load_artist_data(segments, query, openai_key):
    # Read biography
    if "biography" in segments:
        with open("backend/artistData/biography.txt", "r") as file:
            biography = file.read()
    else:
        biography = ""
        
    if "lyrics" in segments:
        song_title = get_song_info(query, openai_key)
        lyrics = load_lyrics(song_title)

    # Fetch Album Data from Spotify API
    if "album_data" in segments:
        album_data = load_album_data()

    return {
        "biography": biography,
        "album_data": album_data,
        "lyrics": lyrics
    }

def load_lyrics(song_title):
    with open(f"backend/artistData/lyrics/{song_title}.txt", "r") as file:
        lyrics = file.read()
    return lyrics

def load_album_data():
    album_data = get_spotify_data
    return album_data