from flask import Flask,request,redirect
from twilio.twiml.messaging_response import MessagingResponse
from cleverwrap import CleverWrap
from config import api_key

app=Flask(__name__)
clever_bot_api=CleverWrap(api_key)

@app.route("/sms",methods=["POST","GET"])
def sms_reply():
    message_body=request.form["Body"]
    clever_bot_response=clever_bot_api.say(message_body)

    resp=MessagingResponse()
    resp.message(clever_bot_response)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
