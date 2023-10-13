from chatBots.getAnswerWithContext import get_answer_with_context
from controller.controller import validate_user_input


def websideAI(user_query):
    print("Starting AI")

    response = validate_user_input(user_query)

    return response
