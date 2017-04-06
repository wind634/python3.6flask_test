from flask import Flask
from flask import flash
from flask import redirect
from flask import request
from flask import url_for
from flask_login import current_user
from flask_principal import identity_loaded, UserNeed, RoleNeed
from flask_uploads import configure_uploads, UploadSet, patch_request_class

from app.extensions.admin_ext import admin
from app.extensions.openid_ext import oid
from app.extensions.babel_ext import babel
from app.extensions.cache_ext import cache
from app.extensions.database_ext import db
from app.extensions.login_ext import login_manager
from app.extensions.principal_ext import principals
from app.extensions.uploads_ext import photos
from app.modules.user.models import User
from app.modules.user.views import admin_user_blueprint
from config.config import config_settings
from flask import g, session

ADMIN_BLUEPRINTS = (
    (admin_user_blueprint, "/admin"),
    # (admin_user_blueprint, "/"),
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
    # 国际化
    config_babel(app)
    # 缓存
    cache.init_app(app)
    # openid
    # config_openid(app)
    # 权限设置
    config_principals(app)
    
    # 配置上传插件
    configure_uploads(app, photos)
    # 限制上传文件大小 1 * 1024 * 1024 1M
    # patch_request_class(app, 1 * 1024)
    # 配置admin
    admin.init_app(app)


def config_babel(app):
    """
    配置babel
    :param app:
    :return:
    """
    babel.init_app(app)
    
    @babel.localeselector
    def get_locale():
        # if a user is logged in, use the locale from the user settings
        user = getattr(g, 'user', None)
        if user is not None:
            return user.locale
        # otherwise try to guess the language from the user accept
        # header the browser transmits.  We support de/fr/en in this
        # example.  The best match wins.
        # 根据浏览器头来判断返回
        # return request.accept_languages.best_match(['de', 'fr', 'en'])
        # return request.accept_languages.best_match(['zh_Hans_CN'])
        return 'zh_Hans_CN'
    
    @babel.timezoneselector
    def get_timezone():
        user = getattr(g, 'user', None)
        if user is not None:
            return user.timezone


def config_openid(app):
    oid.init_app(app)
    
    @app.before_request
    def lookup_current_user():
        g.user = None
        if 'openid' in session:
            print("'openid' in session")
            openid = session['openid']
            g.user = User.query.filter_by(openid=openid).first()
    
    @oid.after_login
    def after_login(resp):
        print("after_login...")
        session['openid'] = resp.identity_url
        user = User.query.filter_by(openid=resp.identity_url).first()
        if user is not None:
            flash(u'Successfully signed in')
            g.user = user
            return redirect(oid.get_next_url())
        return redirect(url_for('create_profile', next=oid.get_next_url(),
                                name=resp.fullname or resp.nickname,
                                email=resp.email))


def config_principals(app):
    principals.init_app(app)
    
    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        """Change the role via add the Need object into Role.

           Need the access the app object.
        """
        # Set the identity user object
        identity.user = current_user

        # Add the UserNeed to the identity user object
        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        # Add each role to the identity user object
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))


    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        # Set the identity user object
        identity.user = current_user
    
        # Add the UserNeed to the identity user object
        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))
    
        # Add each role to the identity user object
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))