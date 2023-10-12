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

class SpotifyData:
    
    def __init__(self, artist_name):
        print("Loading up SPOTIFY DATA CLASS")
        self.artist_name = artist_name
        self.artist_id, self.artist_genres = self.get_artist_id()
        self.discography = self.get_discography()

    def get_artist_id(self):
        results = sp.search(q=self.artist_name, type="artist")
        artist = results["artists"]["items"][0]
        return artist["id"], artist["genres"]

    def get_discography(self):
        album_types = ["album", "single"]
        discography = []

        for album_type in album_types:
            albums = sp.artist_albums(self.artist_id, album_type=album_type)

            for album in albums["items"]:
                album_id = album["id"]
                album_data = {
                    "album_name": album["name"],
                    "release_date": album["release_date"],
                    "tracks": [],
                    "genres": self.artist_genres,
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

    def get_all_track_names(self):
        all_tracks = []

        for album in self.discography:
            for track in album["tracks"]:
                all_tracks.append(track["track_name"])

        return all_tracks
    
    def song_released_by_artist(self, track_name):
        all_tracks = self.get_all_track_names()
        result =  track_name.lower() in (track.lower() for track in all_tracks)
        return result
