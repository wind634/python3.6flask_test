from flask import Blueprint

from app.modules.user.views import login

admin_user_blueprint = Blueprint("admin_user", __name__)

url_rule_list = [
    # 路径 endpoint  views_func
    ('/', 'index', login)
]

for url_rule in url_rule_list:
    admin_user_blueprint.add_url_rule(url_rule[0], url_rule[1], url_rule[2])
