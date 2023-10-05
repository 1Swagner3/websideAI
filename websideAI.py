import os
from dotenv import load_dotenv
from functions.getAnswerWithContext import get_answer_with_context


# Manually load the .env file (if you're using python-dotenv)
load_dotenv()

# Fetch the OpenAI key
openai_key = os.environ.get("OPENAI_KEY")


def websideAI():
    print("Starting AI")
    user_query = input("Enter query: ")

    result = get_answer_with_context(user_query, openai_key)
    
    print(result)


if __name__ == "__main__":
    websideAI()
