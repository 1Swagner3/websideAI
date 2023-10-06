import os
from dotenv import load_dotenv
from functions.getAnswerWithContext import get_answer_with_context



# Manually load the .env file (if you're using python-dotenv)
load_dotenv()

# Fetch the OpenAI key
openai_key = os.environ.get("OPENAI_KEY")


def websideAI(user_query):
    print("Starting AI")
    
    if user_query.lower() in ["exit", "quit"]:
        return "Goodbye!"
        
    response = get_answer_with_context(user_query, openai_key)
        
    return response