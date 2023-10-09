def format_song_title(title):
    extracted_title = title.split("\"")[-2]
    return extracted_title.lower().replace(" ", "_")