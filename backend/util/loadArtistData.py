from util.getSpotifyData import get_spotify_data
from chatBots.getSongInfo import get_song_info
from util.formatSongTitle import format_song_title

def load_artist_data(segments, query):
    # Load Biography
    if "biography" in segments:
        with open("./artistData/biography.txt", "r") as file:
            biography = file.read()
    else:
        biography = ""
        
    # Load Song Lyrics
    if "lyrics" in segments:
        song_data = get_song_info(query)
        lyrics = load_lyrics(song_data.songName)
        song_data.lyrics = lyrics
    else:
        song_data = {} 

    # Fetch Album Data from Spotify API
    if "album_data" in segments:
        album_data = load_album_data()
    else:
        album_data = {}

    return {
        "biography": biography,
        "album_data": album_data,
        "lyrics": song_data
    }

def load_lyrics(song_title):
    
    try:
        formatted_song_title = format_song_title(song_title)
        with open(f"./artistData/lyrics/{formatted_song_title}.txt", "r") as file:
            lyrics = file.read()
            print("Loaded lyrics SUCCESSFULLY")
    except:
        lyrics = ""
        print("Fails to load lyrics of title: ", format_song_title(song_title))
        
    return lyrics

def load_album_data():
    album_data = get_spotify_data
    return album_data