from flask import Flask, render_template, request, jsonify
import requests
import json
import os

app2 = Flask(__name__)
app2.static_folder = 'static'

API_URL = "https://flowisetest-1.onrender.com/api/v1/prediction/dbaf12c5-c585-42e3-a057-ce4e41dbbd26"

def query(payload):
    response = requests.post(API_URL, json=payload)
    try:
        response_json = response.json()
        return response_json
    except json.JSONDecodeError:
        return {"error": "Invalid response from API"}

@app2.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input.strip() != "":
            response = query({"question": user_input})
            bot_response = response.get("text")
            return render_template("index.html", user_input=user_input, bot_response=bot_response)
    return render_template("index.html", user_input="", bot_response="")

@app2.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form.get("user_input")
    if user_input.strip() != "":
        response = query({"question": user_input})
        bot_response = response.get("text")
        return jsonify({"bot_response": bot_response})
    return jsonify({"bot_response": ""})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app2.run(host='0.0.0.0', port=port)