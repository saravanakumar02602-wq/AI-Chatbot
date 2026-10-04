from flask import Flask, jsonify, render_template, request


from chatbot import Chatbot
from knowledge_base import KB

app = Flask(__name__)
bot = Chatbot(KB)


@app.get("/")
def home():
    return render_template("index.html", starters=bot.starters)


@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()[:200]
    if not message:
        return jsonify(error="Please type a message."), 400
    return jsonify(bot.answer(message))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
