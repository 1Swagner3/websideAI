from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import CommaSeparatedListOutputParser

import os
from dotenv import load_dotenv


def get_relevant_segments(query):
    load_dotenv()
    openai_key = os.environ.get("OPENAI_KEY")
    
    output_parser = CommaSeparatedListOutputParser()
    format_instructions = output_parser.get_format_instructions()
    
    print("starting relevant segment search")
    llm = ChatOpenAI(
        openai_api_key=openai_key, temperature=0.7, model_name="gpt-3.5-turbo"
    )

    prompt = PromptTemplate(
        template="""
        You are the assitant of the solo music artist SicHat. The user is visiting SicHat's webside to learn more about the Artist.
        Given a question about the artist SicHat like {query}, which parts of the artist's background should be included: 
        biography, album_data, lyrics or controversies? 
        Only return a maximum of two selections, separated by a comma without a sentence.
        {format_instructions}
        """,
        input_variables=["query"],
        partial_variables={"format_instructions": format_instructions}
    )
    
    
    prompt.format(query=query)

    chain = LLMChain(llm=llm, prompt=prompt)

    print("loading relevant segments")
    result = chain.run(query)
    segments = output_parser.parse(result)

    print(f"segments found: {segments}")
    return segments
