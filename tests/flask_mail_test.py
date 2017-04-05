from flask import Flask
from flask_mail import Mail

# app = Flask(__name__)
from app import create_app
from threading import Thread


app = create_app('default')
mail = Mail(app)

from flask_mail import Message


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
        

@app.route("/")
def index():
    msg = Message("关于重要事情的商讨通知",
                  recipients=["2911184332@qq.com"])
    # with app.open_resource("../tests/test.jpeg") as fp:
    #     msg.attach("test.jpeg", "image/jpeg", fp.read())
    # msg.body = "我爱你"
    msg.html = "<b>我爱你</b>"
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    # mail.send(msg)
    return "hello"

app.run(debug=True)