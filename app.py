from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

API_URL = "https://flowisetest-1.onrender.com/api/v1/prediction/318e37be-4ab4-4d78-9c3f-791f977fe11b"

def query(payload):
    response = requests.post(API_URL, json=payload)
    try:
        response_json = response.json()
        return response_json
    except json.JSONDecodeError:
        return {"error": "Invalid response from API"}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input.strip() != "":
            response = query({"question": user_input})
            bot_response = response.get("text")
            return render_template("index.html", user_input=user_input, bot_response=bot_response)
    return render_template("index.html", user_input="", bot_response="")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form.get("user_input")
    if user_input.strip() != "":
        response = query({"question": user_input})
        bot_response = response.get("text")
        return jsonify({"bot_response": bot_response})
    return jsonify({"bot_response": ""})

if __name__ == "__main__":
    app.run(debug=True)