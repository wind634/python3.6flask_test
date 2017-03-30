from flask_login import LoginManager

login_manager = LoginManager()

login_manager.login_view = 'auth.login'
login_manager.login_message = u"你没有登录，请先登陆"
login_manager.login_message_category = "error"


@login_manager.user_loader
def load_user(user_id):
    from app.modules.user.models import User
    return User.query.get(user_id)