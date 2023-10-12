from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from util.getSpotifyData import get_spotify_data
from util.formatSongTitle import format_song_title
from langchain.output_parsers import PydanticOutputParser
from langchain.pydantic_v1 import BaseModel, Field, validator
from util.getSpotifyData import get_all_track_names
import os
from dotenv import load_dotenv


class Song(BaseModel):
    songName: str = Field(description="name of the song")
    songURL: str = Field(description="spotify url to the song")
    songInAlbumData: bool = Field(
        default=False, description="Is the song in album data"
    )
    lyrics: str = Field(default=None, description="Lyrics of the song")

    @validator("songInAlbumData", pre=True, always=True)
    def check_if_song_is_in_song_list(cls, songInAlbumData, values):
        songName = values.get("songName")
        songList = get_all_track_names()
        return songName in songList


def get_song_info(query):
    load_dotenv()
    openai_key = os.environ.get("OPENAI_KEY")

    print("query song info bot")
    llm = ChatOpenAI(
        openai_api_key=openai_key, temperature=0.2, model_name="gpt-3.5-turbo"
    )

    print("calling spotify api")
    artist_data = get_spotify_data()

    parser = PydanticOutputParser(pydantic_object=Song)

    prompt = PromptTemplate(
        input_variables=["artist_data", "query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
        template="""
        Given the user query "{query}", identify which song from SicHat's discography best matches the query.
        Using the provided discography data: {artist_data}.

        Please respond with the following format:
        songName: [name of the song]
        songURL: [spotify url to the song]
        songInAlbumData: [true/false if the song is in album data]
        lyrics: [lyrics of the song, if available]
        
        {format_instructions}
     """,
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    result = chain.run({"artist_data": artist_data, "query": query})
    print("PROMPT RESULT :", result)

    song_data = parser.parse(result)
    print("Parser RESULT: ", song_data)

    return song_data
