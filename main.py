import os
from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
from dotenv import load_dotenv
from utils import log_call_details

load_dotenv()

app = Flask(_name_)

@app.route("/voice", methods=["POST"])
def voice():
    caller = request.form.get("From", "unknown")
    log_call_details(caller)

    resp = VoiceResponse()
    resp.say("Hello! You've reached the AI-powered voice assistant.")
    resp.pause(length=1)
    resp.say("Please say your request after the beep. Goodbye!", voice='alice')
    return Response(str(resp), mimetype="application/xml")

if _name_ == "_main_":
    app.run(port=5000)