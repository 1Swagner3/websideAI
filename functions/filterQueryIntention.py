from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def filter_query_intention(query, openai_key):
    print("starting intention filter")
    llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.7, model_name="gpt-3.5-turbo")

    prompt = PromptTemplate(
        input_variables=["query"],
        template="""
        Given the user's question "{query}", determine if this question pertains to the artist known as 'SicHat' or any common variations like 'sichat', 'sic hat', etc. 
        Is the question about this artist? Respond with 'True' or 'False'.
        """,
    )
    chain = LLMChain(llm=llm, prompt=prompt)

    print("determin interaction type")
    result = chain.run({"query": query})

    print(f"interaction type: {result}")
    return result
