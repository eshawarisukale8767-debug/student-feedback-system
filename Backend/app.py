from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Student Feedback API is running!"


@app.route("/feedback", methods=["POST"])
def feedback():

    data = request.json

    name = data.get("name")
    rating = data.get("rating")
    message = data.get("message")

    return jsonify({
        "success": True,
        "response": f"Thank you {name}! Your rating is {rating}/5. Feedback received successfully."
    })


if __name__ == "__main__":
    app.run(debug=True)