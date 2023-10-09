from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from chatBots.getRelevantSegments import get_relevant_segments
from util.loadArtistData import load_artist_data
from chatBots.getSongInfo import get_song_info


def get_answer_with_context(query, openai_key):
    print("loading answer engine")
    llm = ChatOpenAI(
        openai_api_key=openai_key, temperature=0.7, model_name="gpt-3.5-turbo"
    )

    segments = get_relevant_segments(query, openai_key)

    print("load artist data")
    artist_data = load_artist_data()
    context_data = {segment: artist_data.get(segment, "") for segment in segments}

    if "lyrics" in segments:
        result = get_song_info(query, openai_key)

    prompt = PromptTemplate(
        input_variables=["contextData", "query"],
        template="""
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
