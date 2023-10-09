from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from util.getSpotifyData import get_spotify_data


def get_song_info(query, openai_key):
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
        Using the provided discography data: {artist_data},
        please ONLY return the song title that best matches the query without any additional text. Dont provide any context. 
     """,
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({"artist_data": artist_data, "query": query})
    song_title = result.split('"')[-2]
    print("found song: ", song_title)
    return result
