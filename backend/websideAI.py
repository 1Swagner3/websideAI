from chatBots.getAnswerWithContext import get_answer_with_context
from controller.controller import validate_user_input


def websideAI(user_query):
    print("Starting AI")

    if user_query.lower() in ["exit", "quit"]:
        return "Goodbye!"

    response = validate_user_input(user_query)

    return response
