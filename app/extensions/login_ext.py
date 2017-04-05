from flask_login import LoginManager

login_manager = LoginManager()

# 登录视图的名称
login_manager.login_view = 'auth.login'
# 没有登陆情况下默认的闪现消息
login_manager.login_message = u"你没有登录，请先登陆"
# 自定义消息分类
login_manager.login_message_category = "error"


@login_manager.user_loader
def load_user(user_id):
    from app.modules.user.models import User
    return User.query.get(user_id)