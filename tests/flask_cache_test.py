import random

from flask import Flask
from flask_mail import Mail

# app = Flask(__name__)
from app import create_app
from app.extensions.cache_ext import cache

app = create_app('default')
mail = Mail(app)


with app.app_context():
    @cache.memoize(timeout=50)
    def big_foo(a, b):
        return a + b + random.randrange(0, 1000)
    print(big_foo(5, 2))
    print(big_foo(5, 3))
    cache.delete_memoized('big_foo')
    print(big_foo(5, 2))


# @app.route("/")
# @cache.cached(timeout=50)
# def index():
#
#     return "hello"
#
# app.run(debug=True)