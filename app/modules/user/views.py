from flask import render_template
from flask import request
from flask_login import login_user, current_user

from app.modules.user.forms import UserForm
from app.modules.user.models import User
from flask import Blueprint
from flask_babel import gettext as _

# 蓝图
admin_user_blueprint = Blueprint("admin_user", __name__)


@admin_user_blueprint.route('/', endpoint='login_index')
def login_index():
    s = _("爱情")
    print(s)
    return render_template('index.html')


@admin_user_blueprint.route('/login', endpoint='login',  methods=['GET', 'POST'])
def login():
    
    if request.method == "GET":
        if current_user.is_authenticated:
            return "已登录"
        else:
            return "未登录"
    else:
        # 获取post过来的参数
        # 启用或禁用csrf保护
        form = UserForm(csrf_enabled=False)
        if form.validate_on_submit():
            return "验证成功"
        else:
            print(form.errors)
            return "验证失败"
        # name = request.form.get('username')
        # password = request.form.get('password')
    
        user = User.query.first()
        login_user(user)
        return render_template('login_success.html')
