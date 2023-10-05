from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from functions.getRelevantSegments import get_relevant_segments
from functions.loadArtistData import load_artist_data

def get_answer_with_context(query, openai_key):
    print("loading answer engine")
    llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.7, model_name="gpt-3.5-turbo")


    segments = get_relevant_segments(query, openai_key)

    print("load artist data")
    artist_data = load_artist_data()
    context_data = {segment: artist_data.get(segment, "") for segment in segments}

    prompt = PromptTemplate(
        input_variables=["contextData", "query"],
        template="""
        {contextData}
        
        Given the provided data, answer the querstion: {query} - about the artist SicHat.                            
        """,
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    print("quering ai")
    result = chain.run({"contextData": context_data, "query": query})

    return result
