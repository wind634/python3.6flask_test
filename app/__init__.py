from flask import Flask
from app.extensions.database import db
from app.extensions.login import login_manager
from app.modules.user.views import admin_user_blueprint
from config.config import config_settings

ADMIN_BLUEPRINTS = (
    (admin_user_blueprint, "/admin"),
)


def configure_admin_blueprints(app):
    for blueprint, url_prefix in ADMIN_BLUEPRINTS:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
        

def _set_allow_origin(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


def create_app(config_name):
    app = Flask(__name__, template_folder='templates',
                static_folder='static')
    # 从配置文件中加载配置
    app.config.from_object(config_settings[config_name])
    # 初始化配置
    config_settings[config_name].init_app(app)
    # 初始化扩展
    configure_extensions(app)
    # 初始化蓝图
    configure_admin_blueprints(app)
    
    if app.config.get("DEBUG"):
        # 允许跨域ajax请求
        app.after_request(_set_allow_origin)
    return app


def configure_extensions(app):
    # 初始化数据库
    db.init_app(app)
    # 初始化用户登录
    login_manager.init_app(app)
