flask搭建框架要点小计
1. Flask 开发环境下静态文件的配置:
    /static/即可
2. Flask-Login
    flask登录插件的配置和使用
3. Flask-Script使用
    略
4. PyMySQL代替 python-mysql
5. 使用Flask-WTF
    启用或禁用csrf保护
    form = UserForm(csrf_enabled=False)
6. 使用Flask-Migrate
    命令 python manage.py db init 第一次使用时初始化
    创建迁移文件 python manage.py db migrate -m "initial migration"
    执行迁移  python manage.py db upgrade


