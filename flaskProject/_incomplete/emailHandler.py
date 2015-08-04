#!/usr/bin/env python

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)

### CONFIGURE
DEBUG = True,
MAIL_SERVER = 'smtp.gmail.com',
MAIL_PORT = 465,
MAIL_USE_SSL = True,
MAIL_USE_TLS =False,
MAIL_USERNAME = 'gzakkg@gmail.com',
MAIL_PASSWORD = raw_input("Input pass:"),
DEFAULT_MAIL_SENDER = 'gzakkg@gmail.com'

mail=Mail(app)

@app.route("/")
def index():
    msg = Message(
        "Hello",
        # sender='gzakkg@gmail.com',
        recipients=
        ["gzakkg@gmail.com",
        "rhayes777@gmail.com"])
    msg.body = "This is the email body"
    mail.send(msg)
    return "Sent"

if __name__ == "__main__":
    app.run()

