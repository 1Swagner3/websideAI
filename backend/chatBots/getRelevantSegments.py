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
        openai_api_key=openai_key, temperature=0.4, model_name="gpt-3.5-turbo"
    )

    prompt = PromptTemplate(
        template="""
        You are the assitant of the solo music artist SicHat. The user is visiting SicHat's webside to learn more about the Artist.
        Given a question about the artist SicHat like {query}, which of the following topics fits best: 
        biography, album_data, lyrics, controversies or general interactions (like greetings etc.)? 
        Return two sections.
        
        Here is was description about what the different sections contain: 
        Biography: Information about how SicHat began. No information about songs or lyrics. 
        Album Data: The entire discography of the artist. Songs that are not listed here were not released by the artist
        Lyrics: Lyrics and other helpful song data to a song that the user might requested information about. 
        Controversies: Controversal topics and opinions about the artist.
        
        {format_instructions}
        """,
        input_variables=["query"],
        partial_variables={"format_instructions": format_instructions},
    )

    prompt.format(query=query)

    chain = LLMChain(llm=llm, prompt=prompt)

    print("loading relevant segments")
    result = chain.run({"query": query})
    segments = output_parser.parse(result)

    print(f"segments found: {segments}")
    return segments
