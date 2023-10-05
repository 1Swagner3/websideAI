import json
from functions.albumToText import json_to_text


def load_artist_data():
    # Read biography
    with open("./artistData/biography.txt", "r") as file:
        biography = file.read()

    # Read and convert lyrics JSON to text
    with open("./artistData/album.json", "r") as file:
        lyrics_data = json.load(file)
        lyrics = json_to_text(lyrics_data)

    # Add more as needed

    return {
        "biography": biography,
        "lyrics": lyrics,
        # ...
    }
