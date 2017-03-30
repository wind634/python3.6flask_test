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
    validate validate_on_submit 有一些微小区别
    如何从form直接保存对象?

6. 使用Flask-Migrate
    命令 python manage.py db init 第一次使用时初始化
    创建迁移文件 python manage.py db migrate -m "initial migration"
    执行迁移  python manage.py db upgrade
7. flask国际化
    Babel  lask-Babel

    pybabel extract -F babel.cfg -o messages.pot .  / pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .
    pybabel init -i messages.pot -d translations -l de
    pybabel compile -d translations
    # 更新
    pybabel update -i messages.pot -d translations

    # 修改语言后刷新
    user.timezone = request.form['timezone']
    user.locale = request.form['locale']
    refresh()
    flash(gettext('Language was changed'))

8. flask 部署方式总结
    1.apache加mod_wsgi不推荐
    2.使用 uwsgi+nginx来配置





