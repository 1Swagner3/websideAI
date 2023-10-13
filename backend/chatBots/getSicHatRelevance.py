from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from util.segmentsParser import segments_parser
import os
from dotenv import load_dotenv


def get_user_query_relevance_weighted(query):
    print("loading query relevance check")

    load_dotenv()
    openai_key = os.environ.get("OPENAI_KEY")

    llm = ChatOpenAI(
        openai_api_key=openai_key, temperature=0.4, model_name="gpt-3.5-turbo"
    )

    prompt = PromptTemplate(
        template="""
        You are the assistant of the solo music artist SicHat. A user asked: "{query}". 

        Please rate the relevance of the user's query on a scale of 0 to 5, with 0 being irrelevant and 5 being most relevant for the following categories:

        - SicHat: Is the query specifically about SicHat?
        - Greeting: Is it a greeting?
        - Small Talk: Is it general small talk?
        - Irrelevant: Is the query completely irrelevant to SicHat?

        Provide your ratings in the format:
        sichat: [score],
        greeting: [score],
        small_talk: [score],
        irrelevant: [score]
        """,
        input_variables=["query"],
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({"query": query})

    segments = segments_parser(result)

    print(f"QUERY RELEVANCE: {segments}")
    return segments
