from flask_login import UserMixin

from app.extensions.database_ext import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50))
    desc = db.Column(db.String(50))
    sex = db.Column(db.String(10))
    email = db.Column(db.String(120), unique=True)
    openid = db.Column(db.String(120), unique=True)
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
        
    def is_anonymous(self):
        return False
    
    def get_id(self):
        try:
            return text_type(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')
    
    def __repr__(self):
        return '<User %r>' % self.name
    
    
text_type = str
