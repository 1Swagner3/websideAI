from chatBots.getRelevantSegments import get_relevant_segments
from util.loadArtistData import load_artist_data
from util.ArtistDataLoader import ArtistDataLoader
from chatBots.songDoesNotExist import generate_song_does_not_exist_response
from chatBots.getAnswerWithContext import get_answer_with_context


def validate_user_input(query):
    segments = get_relevant_segments(query)

    loader = ArtistDataLoader()

    contextData = {}

    if "album_data" in segments or "lyrics" in segments:
        song_data = loader.load_song_data(query)

        if not song_data.songInAlbumData:
            return generate_song_does_not_exist_response(query)

    if "biography" in segments:
        biography = loader.load_biography()
        contextData["biography"] = biography

    if "album_data" in segments:
        album_data = loader.load_album_data()
        contextData["album_data"] = album_data

    if "lyrics" in segments:
        lyrics_data = loader.load_song_lyrics(query)
        contextData["lyrics"] = lyrics_data

    return get_answer_with_context(query, contextData)
