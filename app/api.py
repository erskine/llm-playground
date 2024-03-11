from flask import Flask, jsonify, request
from llm import query

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to Flask", 200


# A route that accepts POST requests, and returns the sent data
@app.route('/ask', methods=['POST'])
def post_data():
    data = request.get_json()  # Assuming the sent data is in JSON format
    question = data["question"]
    answer = query(question)
    return jsonify(answer.response), 201

if __name__ == '__main__':
    app.run(debug=True)
