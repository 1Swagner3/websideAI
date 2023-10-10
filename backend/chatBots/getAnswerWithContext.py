from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from chatBots.getRelevantSegments import get_relevant_segments
from util.loadArtistData import load_artist_data
import os
from dotenv import load_dotenv

def get_answer_with_context(query):
    load_dotenv()
    openai_key = os.environ.get("OPENAI_KEY")
    
    print("loading answer engine")
    llm = ChatOpenAI(
        openai_api_key=openai_key, temperature=0.7, model_name="gpt-3.5-turbo"
    )

    segments = get_relevant_segments(query)

    print("load artist data")
    artist_data = load_artist_data(segments, query)
    context_data = {segment: artist_data.get(segment, "") for segment in segments}

    prompt = PromptTemplate(
        input_variables=["contextData", "query"],
        template="""
        You are the assitant of the solo music artist SicHat. The user is visiting SicHat's webside to learn more about the Artist.
        Given a human interaction with the query: "{query}", respond in a conversational manner. 
        If the query diverts too much from the topic of the artist "SicHat", steer the conversation back towards that topic. 
        Do not create fictional personas; respond directly to the query.    
        
        You can use the following context variables: {contextData} to help you answer the query.
        
        Try to keep it short and concise. Unless you are specifically asked to do so.                   
        """,
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    print("quering ai")
    result = chain.run({"contextData": context_data, "query": query})

    return result
