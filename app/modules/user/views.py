from flask import render_template
from flask import request
from flask_login import login_user
from app.modules.user.models import User
from flask import Blueprint

# 蓝图
admin_user_blueprint = Blueprint("admin_user", __name__)


@admin_user_blueprint.route('/', endpoint='login_index')
def login_index():
    
    return render_template('index.html', locals())


@admin_user_blueprint.route('/login', endpoint='login',  methods=['GET','POST'])
def login():
    if request.method == "GET":
        if User.is_authenticated:
            return "已登录"
        else:
            return "未登录"
    else:
        # 获取post过来的参数
        name = request.form.get('username')
        password = request.form.get('password')
    
        user = User.query.first()
        login_user(user)
        return render_template('login_success.html')
