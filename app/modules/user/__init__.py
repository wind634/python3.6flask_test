from flask import Blueprint

# 蓝图
admin_user_blueprint = Blueprint("admin_user", __name__)

from . import views

