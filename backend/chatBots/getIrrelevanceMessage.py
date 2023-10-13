from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from util.segmentsParser import segments_parser
import os
from dotenv import load_dotenv


def get_irrelevance_message(query):
    print("loading irrelevance messanger")

    load_dotenv()
    openai_key = os.environ.get("OPENAI_KEY")

    llm = ChatOpenAI(
        openai_api_key=openai_key, temperature=0.4, model_name="gpt-3.5-turbo"
    )

    prompt = PromptTemplate(
        template="""
        You are the assistant of the solo music artist SicHat. A user asked: "{query}". 
        You were able to determine that the query has nothing to do with SicHat. 
        Formulate an apology that you are unable to process his request because it has nothing to do with SicHat. 
        Keep it short and concise.
        """,
        input_variables=["query"],
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({"query": query})
    return result
