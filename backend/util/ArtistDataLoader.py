from util.getSpotifyData import get_spotify_data
from chatBots.getSongInfo import get_song_info
from util.formatSongTitle import format_song_title


class ArtistDataLoader:
    def __init__(self):
        pass

    def load_biography(self):
        with open("./artistData/biography.txt", "r") as file:
            return file.read()

    def load_song_data(self, query):
        song_data = get_song_info(query)
        return song_data

    def load_song_lyrics(self, query):
        song_data = self.load_song_data(query)
        lyrics = self._load_lyrics_from_file(song_data.songName)
        song_data.lyrics = lyrics
        return song_data

    def load_album_data(self):
        return get_spotify_data()

    def _load_lyrics_from_file(self, song_title):
        try:
            formatted_song_title = format_song_title(song_title)
            with open(f"./artistData/lyrics/{formatted_song_title}.txt", "r") as file:
                lyrics = file.read()
                print("Loaded lyrics SUCCESSFULLY")
                return lyrics
        except:
            print("Fails to load lyrics of title:", format_song_title(song_title))
            return ""
