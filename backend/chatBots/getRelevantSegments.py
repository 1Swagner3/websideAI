from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv


def get_relevant_segments(query):
    load_dotenv()
    openai_key = os.environ.get("OPENAI_KEY")
    
    print("starting relevant segment search")
    llm = ChatOpenAI(
        openai_api_key=openai_key, temperature=0.7, model_name="gpt-3.5-turbo"
    )

    prompt = PromptTemplate.from_template(
        """Given a question about the artist SicHat like {query}, which parts of the artist's background should be included: 
            biography, album_data, lyrics or controversies? 
            Only return a maximum of two selections, separated by a comma without a sentence.
        """
    )
    prompt.format(query=query)

    chain = LLMChain(llm=llm, prompt=prompt)

    print("loading relevant segments")
    result = chain.run(query)

    segments = [segment.strip() for segment in result.split(",")]

    print(f"segments found: {segments}")
    return segments
