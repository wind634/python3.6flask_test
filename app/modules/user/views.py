from flask import abort
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask_uploads import UploadSet
from flask_login import login_user, current_user


from app.extensions.openid_ext import oid
from app.extensions.uploads_ext import photos
from app.modules.user.forms import UserForm
from app.modules.user.models import User
from flask import Blueprint
from flask_babel import gettext as _

from . import admin_user_blueprint


@admin_user_blueprint.route('/sss', endpoint='login_index')
def login_index():
    s = _("爱情")
    print(s)
    return render_template('index.html')


@admin_user_blueprint.route('/login', endpoint='login',  methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None:
        return redirect(oid.get_next_url())
    if request.method == 'POST':
        openid = request.form.get('openid')
        if openid:
            return oid.try_login(openid, ask_for=['nickname', 'email'], ask_for_optional=['fullname'])
    # return render_template('login_success.html')
    
    return render_template('oid_index.html', next=oid.get_next_url(),
                               error=oid.fetch_error())
    # if request.method == "GET":
    #     if current_user.is_authenticated:
    #         return "已登录"
    #     else:
    #         return "未登录"
    # else:
    #     # 获取post过来的参数
    #     # 启用或禁用csrf保护
    #     form = UserForm(csrf_enabled=False)
    #     if form.validate_on_submit():
    #         return "验证成功"
    #     else:
    #         print(form.errors)
    #         return "验证失败"
    #     # name = request.form.get('username')
    #     # password = request.form.get('password')
    #
    #     user = User.query.first()
    #     login_user(user)
    #     return render_template('login_success.html')


# @admin_user_blueprint.route('/create-profile', methods=['GET', 'POST'], endpoint="create_profile")
# def create_profile():
#     if g.user is not None or 'openid' not in session:
#         return redirect(url_for('index'))
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         if not name:
#             flash(u'Error: you have to provide a name')
#         elif '@' not in email:
#             flash(u'Error: you have to enter a valid email address')
#         else:
#             flash(u'Profile successfully created')
#             user = User()
#             user.name = name
#             user.email = email
#             user.openid = session['openid']
#             db.session.add(user)
#             db.session.commit()
#             return redirect(oid.get_next_url())
#     return render_template('create_profile.html', next=oid.get_next_url())
#
#
# @admin_user_blueprint.route('/logout')
# def logout():
#     session.pop('openid', None)
#     flash(u'You were signed out')
#     return redirect(oid.get_next_url())


@admin_user_blueprint.route('/upload', methods=['GET', 'POST'], endpoint='upload')
def upload():
    if request.method == "GET":
        return render_template('upload.html')
    else:
        if 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            flash("Photo saved.")
            return redirect(url_for('admin_user.show', name=filename))
        return "上传成功"


@admin_user_blueprint.route('/photo/<name>')
def show(name):
    if name is None:
        abort(404)
    url = photos.url(name)
    return render_template('show.html', url=url, name=name)