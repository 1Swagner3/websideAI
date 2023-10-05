from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def handle_interaction(query, openai_key):
    print("starting regular interaction handler")
    llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.7, model_name="gpt-3.5-turbo")

    prompt = PromptTemplate(
        input_variables=["query"],
        template="""Given a human interaction with the query: "{query}", respond in a conversational manner. 
        If the query diverts too much from the topic of the artist "SicHat", steer the conversation back towards that topic. 
        Do not create fictional personas; respond directly to the query.
        """,
    )
    chain = LLMChain(llm=llm, prompt=prompt)

    print("handle regular interaction")
    result = chain.run({"query": query})

    return result