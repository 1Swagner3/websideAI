from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from util.segmentsParser import segments_parser

import os
from dotenv import load_dotenv

def get_relevant_segments_weighted(query):
    load_dotenv()
    openai_key = os.environ.get("OPENAI_KEY")

    print("starting relevant segment search")
    llm = ChatOpenAI(
        openai_api_key=openai_key, temperature=0.4, model_name="gpt-3.5-turbo"
    )

    prompt = PromptTemplate(
    template="""
    You are the assistant of the solo music artist SicHat. A user is visiting SicHat's website to learn more about the artist. They asked: "{query}". 

    Please rate the relevance of each topic to the user's query on a scale of 0 to 5, with 0 being irrelevant and 5 being most relevant:

    - Biography: How relevant is the biography of SicHat to the query?
    - Album Data: How relevant is the discography of SicHat to the query?
    - Lyrics: How relevant are the lyrics and song data of SicHat to the query?
    - Controversies: How relevant are the controversies related to SicHat to the query?
    - General Interaction: How relevant are general interactions (like greetings) to the query?

    For example, if the user asked about a specific song's lyrics, you might rate Lyrics as 5 and other topics lower.

    Please provide your ratings in the following format:
    biography: [score],
    album_data: [score],
    lyrics: [score],
    controversies: [score],
    general_interaction: [score]
    """,
    input_variables=["query"])


    chain = LLMChain(llm=llm, prompt=prompt)

    print("loading relevant segments")
    result = chain.run({"query": query})
    print("PROMPT RESULT: ", result)
    
    segments = segments_parser(result)
    print(f"segments found: {segments}")
    
    return segments
