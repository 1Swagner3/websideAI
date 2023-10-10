import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()
# Set up credentials
CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_artist_id(artist_name):
    results = sp.search(q=artist_name, type="artist")
    artist = results["artists"]["items"][0]
    return artist["id"], artist["genres"]


def get_discography(artist_id, artist_genres):
    album_types = ["album", "single"]
    discography = []

    for album_type in album_types:
        albums = sp.artist_albums(artist_id, album_type=album_type)

        for album in albums["items"]:
            album_id = album["id"]
            album_data = {
                "album_name": album["name"],
                "release_date": album["release_date"],
                "tracks": [],
                "genres": artist_genres,
            }

            # Fetching tracks for the current album
            tracks = sp.album_tracks(album_id)
            for track in tracks["items"]:
                track_data = {
                    "track_name": track["name"],
                    "duration_ms": track["duration_ms"],
                    "url": track["external_urls"]["spotify"],
                }
                album_data["tracks"].append(track_data)

            discography.append(album_data)

    return discography

def get_all_track_names():
    discography_data = get_spotify_data()
    all_tracks = []

    for album in discography_data:
        for track in album["tracks"]:
            all_tracks.append(track["track_name"])

    return all_tracks


def get_spotify_data():
    artist_name = "SicHat"
    artist_id, artist_genres = get_artist_id(
        artist_name
    )  # Adjust to unpack both ID and genres
    discography_data = get_discography(artist_id, artist_genres)

    return discography_data
