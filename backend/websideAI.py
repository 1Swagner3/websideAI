import os
from dotenv import load_dotenv
from functions.getAnswerWithContext import get_answer_with_context



# Manually load the .env file (if you're using python-dotenv)
load_dotenv()

# Fetch the OpenAI key
openai_key = os.environ.get("OPENAI_KEY")


def websideAI():
    print("Starting AI")
    
    while True:
        user_query = input("\nEnter query (type 'exit' to end): ")

        if user_query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        response = get_answer_with_context(user_query, openai_key)
        
        print(response)


if __name__ == "__main__":
    websideAI()
