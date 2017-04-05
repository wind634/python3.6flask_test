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
                  sender="2911184332@qq.com",
                  recipients=["2911184332@qq.com"])
    mail.send(msg)
    return "hello"

app.run(debug=True)