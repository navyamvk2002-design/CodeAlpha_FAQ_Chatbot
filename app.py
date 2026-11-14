
from flask import Flask, render_template, request, jsonify
from chatbot import get_answer

# Create Flask application
app = Flask(__name__)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Chatbot API
@app.route("/get_response", methods=["POST"])
def get_response():

    data = request.get_json()
    user_question = data.get("message", "")

    answer = get_answer(user_question)

    return jsonify({"answer": answer})


# Run application
if __name__ == "__main__":
    app.run(debug=True)
