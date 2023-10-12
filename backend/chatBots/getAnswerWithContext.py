from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from chatBots.getRelevantSegments import get_relevant_segments
import os
from dotenv import load_dotenv


def get_answer_with_context(query, context_data):
    load_dotenv()
    openai_key = os.environ.get("OPENAI_KEY")

    print("loading answer engine")
    llm = ChatOpenAI(
        openai_api_key=openai_key, temperature=0.4, model_name="gpt-3.5-turbo"
    )

    prompt = PromptTemplate(
        input_variables=["contextData", "query"],
        template="""
        You are the assitant of the solo music artist SicHat. The user is visiting SicHat's webside to learn more about the Artist.
        Given the query: "{query}", respond in a conversational manner. 
        If the query diverts too much from the topic of the artist "SicHat", steer the conversation back towards that topic. 
        Do not create fictional personas; respond directly to the query.    
        
        You can use the following context variables: {contextData} to help you answer the query.
        
        The context data consists of 4 different topics: 
        Biography: A detailed biography about the artist SicHat
        Album Data: The entire discography of the artist. Songs that are not listed here were not released by the artist
        Lyrics: Lyrics and other helpful song data to a song that the user might requested information about. Make sure to share the song url if one is present. The songInAlbumData flag tells you if the song is actually a song by SicHat. If the flag is false it means that it is NOT a song by SicHat, so tell the user that this is not a song by SicHat. 
        Controversies: Controversal topics and opinions about the artist.
        
        Try to keep it short and concise. Unless you are specifically asked to do so.                   
        """,
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    print("quering ai")
    result = chain.run({"contextData": context_data, "query": query})

    return result
