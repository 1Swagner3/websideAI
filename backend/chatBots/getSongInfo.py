from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from util.getSpotifyData import get_spotify_data
from util.formatSongTitle import format_song_title
import os
from dotenv import load_dotenv


def get_song_info(query):
    load_dotenv()
    openai_key = os.environ.get("OPENAI_KEY")
    
    print("query song info bot")
    llm = ChatOpenAI(
        openai_api_key=openai_key, temperature=0.7, model_name="gpt-3.5-turbo"
    )

    print("calling spotify api")
    artist_data = get_spotify_data()

    prompt = PromptTemplate(
        input_variables=["artist_data", "query"],
        template="""
        Given the user query "{query}", identify which song from SicHat's discography best matches the query.
        Using the provided discography data: {artist_data}.
        Please ONLY return the song title that best matches the query without any additional text. Dont provide any context. 
        Be aware that the user might have spelling errors.
     """,
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    
    result = chain.run({"artist_data": artist_data, "query": query})
    print("PROMPT RESULT :", result)
    
    song_title = format_song_title(result)
    print("found song: ", song_title)
    
    return song_title
