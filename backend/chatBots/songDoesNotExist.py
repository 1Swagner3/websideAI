from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv


def generate_song_does_not_exist_response(query):
    load_dotenv()
    openai_key = os.environ.get("OPENAI_KEY")
    llm = ChatOpenAI(
        openai_api_key=openai_key, temperature=0.4, model_name="gpt-3.5-turbo"
    )

    prompt = PromptTemplate(
        template="""
        You are the assitant of the solo music artist SicHat. The user is visiting SicHat's webside to learn more about the Artist.
        You are given the query:  {query}
        You were able to determine that the requested song does not exist. Meaning SicHat never released a song or album with that name. 
        Write a response to let the user know that this song / album does not exist.
        """,
        input_variables=["query"],
    )

    prompt.format(query=query)

    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({"query": query})
    return result
