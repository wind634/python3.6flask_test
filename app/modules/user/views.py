from flask import abort
from flask import render_template
from flask_login import login_user
from jinja2 import TemplateNotFound
from app.modules.user.models import User


def login():
    
    return render_template('index.html')
