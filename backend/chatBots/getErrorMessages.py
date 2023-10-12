from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

def formulate_error_message(error_type):
    load_dotenv()
    openai_key = os.environ.get("OPENAI_KEY")
    
    llm = ChatOpenAI(
        openai_api_key=openai_key, temperature=0.4, model_name="gpt-3.5-turbo"
    )
    
    if error_type == "timeout":
        template = """
        You are the assitant of the solo music artist SicHat. The user is visiting SicHat's webside to learn more about the Artist.
        The user was ran into a Timeout Error while waiting for his query to be answerd. 
        Formulate a apology that you are unable to process his request in the moment. 
        Keep it short and concise.
        """
    
    if error_type == "exception":
        template="""
        You are the assitant of the solo music artist SicHat. The user is visiting SicHat's webside to learn more about the Artist.
        The user was ran into a Exception while waiting for his query to be answerd. 
        Formulate a apology that an error occured and that he should try again. 
        Keep it short and concise.
        """

    prompt = PromptTemplate(
        template=template,
        input_variables=[]
    )

    print("Querying Error BOt")
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({})
    return result
