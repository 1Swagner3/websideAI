import concurrent.futures
from models.ArtistDataLoader import ArtistDataLoader
from models.SpotifyData import SpotifyData
from chatBots.songDoesNotExist import generate_song_does_not_exist_response
from chatBots.getAnswerWithContext import get_answer_with_context
from chatBots.getErrorMessages import formulate_error_message
from chatBots.getRelevantSegmentsWeighted import get_relevant_segments_weighted
from chatBots.getSicHatRelevance import get_user_query_relevance_weighted
from chatBots.getIrrelevanceMessage import get_irrelevance_message
from chatBots.getQueryTooLongMessage import get_query_too_long_message


def validate_user_input(query, timeout_seconds=120):
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(_validate_user_input_logic, query)
            return future.result(timeout=timeout_seconds)

    except concurrent.futures.TimeoutError:
        print("runtime error")
        return formulate_error_message("timeout")
    except Exception as e:
        print(f"An error occurred: {e}")
        return formulate_error_message("exception")


def _validate_user_input_logic(query):
    
    if len(query) > 500:
        return get_query_too_long_message()

    
    query_relevance = get_user_query_relevance_weighted(query)
    if query_relevance.get("irrelevant", 0) == 5:
        return get_irrelevance_message(query)

    segments = get_relevant_segments_weighted(query)

    spotifyData = SpotifyData("SicHat")
    loader = ArtistDataLoader(spotifyData)

    contextData = {}
    song_data = {}

    if segments.get("album_data", 0) == 5 or segments.get("lyrics", 0) == 5:
        song_data = loader.load_song_data(query)

        if not spotifyData.song_released_by_artist(song_data.song_name):
            return generate_song_does_not_exist_response(query)

    if segments.get("biography", 0) == 5:
        biography = loader.load_biography()
        contextData["biography"] = biography

    if segments.get("album_data", 0) == 5:
        album_data = loader.load_album_data()
        contextData["album_data"] = album_data

    if segments.get("lyrics", 0) == 5:
        lyrics_data = loader.load_song_lyrics(song_data)
        contextData["lyrics"] = lyrics_data

    return get_answer_with_context(query, contextData)
