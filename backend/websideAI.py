from chatBots.getAnswerWithContext import get_answer_with_context


def websideAI(user_query):
    print("Starting AI")

    if user_query.lower() in ["exit", "quit"]:
        return "Goodbye!"

    response = get_answer_with_context(user_query)

    return response
