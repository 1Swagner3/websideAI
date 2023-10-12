import concurrent.futures
from chatBots.getRelevantSegments import get_relevant_segments
from models.ArtistDataLoader import ArtistDataLoader
from models.SpotifyData import SpotifyData
from chatBots.songDoesNotExist import generate_song_does_not_exist_response
from chatBots.getAnswerWithContext import get_answer_with_context
from chatBots.getErrorMessages import formulate_error_message

def validate_user_input(query, timeout_seconds=10):
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
