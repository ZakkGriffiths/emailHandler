import os
from flask import Flask, render_template, redirect
from flask.ext.mail import Mail, Message
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['DEFAULT_MAIL_SUBJECT'] = '[Default email subject]'
app.config['DEFAULT_MAIL_SENDER'] = 'Admin <gzakkg@gmail.com>'
app.config['SECRET_KEY'] = 'random_string'
app.config['DEFAULT_ADMIN'] = 'Admin <gzakkg@gmail.com>'

mail = Mail(app)

if __name__ == '__main__':
    app.run(debug=True)

class PolitburoForm(Form):
    name = StringField('What the fucking hell goes here?')
    submit = SubmitField('Submit')

