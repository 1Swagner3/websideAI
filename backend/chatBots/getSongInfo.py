from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import PydanticOutputParser
from langchain.pydantic_v1 import BaseModel, Field
import os
from dotenv import load_dotenv


class Song(BaseModel):
    song_name: str = Field(description="name of the song")
    song_url: str = Field(description="spotify url to the song")
    lyrics: str = Field(default=None, description="Lyrics of the song")


def get_song_info(query, spotify_data):
    load_dotenv()
    openai_key = os.environ.get("OPENAI_KEY")

    print("query song info bot")
    llm = ChatOpenAI(
        openai_api_key=openai_key, temperature=0.2, model_name="gpt-3.5-turbo"
    )

    artist_data = spotify_data.discography

    parser = PydanticOutputParser(pydantic_object=Song)

    prompt = PromptTemplate(
        input_variables=["artist_data", "query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
        template="""
        Given the user query "{query}", identify which song from SicHat's discography best matches the query.
        Using the provided discography data: {artist_data}.

        Please respond with the following format:
        song_name: [name of the song]
        song_url: [spotify url to the song]
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
