from flask import Flask, request, jsonify
from flask_cors import CORS
from websideAI import websideAI

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def ask():
    data = request.get_json()
    user_query = data["query"]

    response = websideAI(user_query)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(port=5000)
