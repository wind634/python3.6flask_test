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
    1. apache加mod_wsgi不推荐
    2. 使用 uwsgi+nginx来配置
    3. gunicorn + gevent

    有代理存在的时候注意设置
        proxy_set_header   Host             $host;
        proxy_set_header   X-Real-IP        $remote_addr;
        proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
    4. tornado

9. 如何打python包
    完成
    sudo python3.6 setup.py sdist
    sudo python3.6 setup.py bdist_egg

10. 如何编写flask插件
    略

11. flask sql_chamely扩展学习
    一对多关系:
        多的一方:
        category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
        category = db.relationship('Category',
            backref=db.backref('posts', lazy='dynamic'))
        多对多要新建表:

    sqlchamely

12. flask - restful
    熟悉使用

13. Flask-Mail
    发邮件的扩展使用
    批量发送
    异步发送
    已完成

14. flask cache的使用
    @cache.cached(timeout=50)
    @cache.memoize(timeout=50)
    完成

15. flask_openid的使用
    另一种登录形式 openid
    
16. flask_principal的使用
    flask权限控制

    login_user(user)

    identity_changed.send(
        current_app._get_current_object(),
        identity=Identity(user.id))

    logout_user()
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)
    identity_changed.send(
        current_app._get_current_object(),
        identity=AnonymousIdentity())

17. flask_uploads 上传文件
    

18. flask-admin

19. abu.admin





