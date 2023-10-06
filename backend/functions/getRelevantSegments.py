from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def get_relevant_segments(query, openai_key):
    print("starting relevant segment search")
    llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.7, model_name="gpt-3.5-turbo")


    prompt = PromptTemplate.from_template(
        "Given a question about an artist like {query}, which parts of the artist's background should be included: biography, album, collaborations, concerts, or controversies? Only return a maximum of two selections, separated by a comma without a sentence."
    )
    prompt.format(query=query)

    chain = LLMChain(llm=llm, prompt=prompt)

    print("loading relevant segments")
    result = chain.run(query)

    segments = [segment.strip() for segment in result.split(",")]

    print(f"segments found: {segments}")
    return segments
