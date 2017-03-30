from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = StringField('密码')

    