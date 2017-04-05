import os

from config.common import Config, basedir


class DevelopmentConfig(Config):
    DEBUG = True

    # 邮件相关
    # QQ邮箱配置
    # MAIL_SERVER = 'smtp.qq.com'
    # MAIL_PORT = 25
    # MAIL_USE_TLS = True
    # MAIL_USE_SSL = False
    # MAIL_USERNAME = "2911184332"
    # MAIL_PASSWORD = "odyhwfarrbzcdfhb"
    # MAIL_PASSWORD = "1991620wind634"

    # 163邮箱配置
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = "nichentianxia11@163.com"
    MAIL_PASSWORD = "1991620wind634"

    MAIL_DEFAULT_SENDER = "nichentianxia11@163.com"
    
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # 邮件相关

    DATABASE_HOST = 'localhost'
    DATABASE_PORT = 3306

    DATABASE_USER = 'root'
    DATABASE_PWD = '634235'
    DATABASE_NAME = 'newtest'

    SQLALCHEMY_DATABASE_URI = 'mysql://' + DATABASE_USER + ':' + DATABASE_PWD + '@' + \
                              DATABASE_HOST + ':' + str(DATABASE_PORT) + '/' + DATABASE_NAME + '?charset=utf8'
    
    
    
    