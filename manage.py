#!/usr/bin/env python3.6

from app import create_app
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.extensions.database_ext import db




__author__ = "wind634"

app = create_app('default')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("runserver", Server('0.0.0.0', port=app.config.get('PORT', 9000)))
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def profile(length=25, profile_dir=None):
    """Start the application under the code profiler."""
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length],
    profile_dir=profile_dir)
    app.run()


@manager.command
def deploy():
    """Run deployment tasks."""
    from flask.ext.migrate import upgrade
    # from app.models import Role, User
    # 把数据库迁移到最新修订版本
    upgrade()
    # 创建用户角色 Role.insert_roles()
    # 让所有用户都关注此用户 User.add_self_follows()

if __name__ == "__main__":
    manager.run()
