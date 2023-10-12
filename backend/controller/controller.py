from chatBots.getRelevantSegments import get_relevant_segments
from models.ArtistDataLoader import ArtistDataLoader
from models.SpotifyData import SpotifyData
from chatBots.songDoesNotExist import generate_song_does_not_exist_response
from chatBots.getAnswerWithContext import get_answer_with_context


def validate_user_input(query):
    segments = get_relevant_segments(query)

    spotifyData = SpotifyData("SicHat")
    loader = ArtistDataLoader(spotifyData)
    
    contextData = {}
    song_data = {}
    
    if "album_data" in segments or "lyrics" in segments:
        song_data = loader.load_song_data(query)
        
        if not spotifyData.song_released_by_artist(song_data.song_name):
            return generate_song_does_not_exist_response(query)

    if "biography" in segments:
        biography = loader.load_biography()
        contextData["biography"] = biography

    if "album_data" in segments:
        album_data = loader.load_album_data()
        contextData["album_data"] = album_data

    if "lyrics" in segments:
        lyrics_data = loader.load_song_lyrics(song_data)
        contextData["lyrics"] = lyrics_data

    return get_answer_with_context(query, contextData)
