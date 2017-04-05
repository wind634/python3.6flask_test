from flask_sqlalchemy import SQLAlchemy

from app import create_app
from app.modules.user.models import User

app = create_app('default')
db = SQLAlchemy(app)

from datetime import datetime


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80))
#     body = db.Column(db.Text)
#     pub_date = db.Column(db.DateTime)
#
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     category = db.relationship('Category',  backref=db.backref('posts', lazy='dynamic'))
#
#     def __init__(self, title, body, category, pub_date=None):
#         self.title = title
#         self.body = body
#         if pub_date is None:
#             pub_date = datetime.utcnow()
#         self.pub_date = pub_date
#         self.category = category
#
#     def __repr__(self):
#         return '<Post %r>' % self.title
#
#
# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return '<Category %r>' % self.name
#
# # db.create_all()
#
# py = Category('Python')
# p = Post('Hello Python', 'Python is pretty cool', py)
# db.session.add(py)
# db.session.add(p)
#
# print(py.posts.all())

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    # addresses = db.relationship('Address', backref='person',
    #                             lazy='dynamic')


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    # person = db.relationship('Person',  backref=db.backref('addresses', lazy='dynamic'))
    person = db.relationship('Person',  backref=db.backref('addresses', lazy='dynamic'))
    # person = db.relationship('Person', backref='addresses')

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<Address %r>' % self.email

    
p = Person.query.get(1)
print(p.name)


# print(p.id)
# db.session.add(p)
# db.session.commit()
# print(p.id)
# a = Address("abc")
# b = Address("abcd")
# a.person = p
# b.person = p
# print(p.addresses.all())


# tags = db.Table('tags',
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
#     db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
# )
#
# class Page(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tags = db.relationship('Tag', secondary=tags,
#         backref=db.backref('pages', lazy='dynamic'))
#
# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#
#
# db.create_all()
