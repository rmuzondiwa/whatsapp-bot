from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hi' in incoming_msg:
        msg.body("Welcome 👋\n1. Products\n2. Prices\n3. Contact")
    elif '1' in incoming_msg:
        msg.body("We sell cement and bricks.")
    elif '2' in incoming_msg:
        msg.body("Prices start from $10.")
    else:
        msg.body("Type 1, 2 or hi")

    return str(resp)

@app.route("/")
def home():
    return "Bot is running!"
