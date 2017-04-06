from flask_admin import BaseView
from flask_admin import expose
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin

from app.modules.user.models import User
from app.extensions.database_ext import db

admin = Admin(name='microblog', template_mode='bootstrap3')


class MyView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return "no access"
    
    @expose('/')
    def index(self):
        return self.render('admin/myindex.html')

admin.add_view(MyView(name='Hello'))
admin.add_view(MyView(name='Hello 1', endpoint='test1', category='Test'))
admin.add_view(MyView(name='Hello 2', endpoint='test2', category='Test'))
admin.add_view(MyView(name='Hello 3', endpoint='test3', category='Test'))


class UserView(ModelView):
    can_delete = False
    column_searchable_list = ['email']
    
admin.add_view(UserView(User, db.session))

