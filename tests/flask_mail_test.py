from flask import Flask
from flask_mail import Mail

# app = Flask(__name__)
from app import create_app

app = create_app('default')
mail = Mail(app)

from flask_mail import Message


@app.route("/")
def index():
    msg = Message("Hello",
                  sender="from@example.com",
                  recipients=["to@example.com"])
    mail.send(msg)
    return "hello"

app.run(debug=True)