def json_to_text(data):
    result = []

    # Extract general details
    name = data.get("name", "")
    release = data.get("release", "")
    duration = data.get("duration", "")

    result.append(
        f"The album '{name}' was released on {release} and has a total duration of {duration}."
    )

    # Extract song details
    songs = data.get("songs", {})
    for song_key, song_data in songs.items():
        song_name = song_data.get("song_name", "")
        song_duration = song_data.get("song_duration", "")
        song_lyrics = song_data.get("song_lyrics", "")
        song_topic = song_data.get("song_topic", "")
        song_emotions = song_data.get("song_emotions", "")

        song_description = (
            f"Song '{song_name}' has a duration of {song_duration}. "
            f"It primarily focuses on the topic of {song_topic} and evokes feelings of {song_emotions}. "
            f"The lyrics go as follows: {song_lyrics}"
        )

        result.append(song_description)

    return "\n\n".join(result)