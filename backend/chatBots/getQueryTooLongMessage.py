from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from util.segmentsParser import segments_parser
import os
from dotenv import load_dotenv


def get_query_too_long_message():
    print("loading QUERY TOO LONG messanger")

    load_dotenv()
    openai_key = os.environ.get("OPENAI_KEY")

    llm = ChatOpenAI(
        openai_api_key=openai_key, temperature=0.4, model_name="gpt-3.5-turbo"
    )

    prompt = PromptTemplate(
        template="""
        You are the assistant of the solo music artist SicHat. 
        The user did input a query that is outside the query input length constrains. 
        Let the user know that the query is too long and can not be processed.
        Keep it short and concise.
        """,
        input_variables=[]
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({})
    return result
