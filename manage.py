#!/usr/bin/env python3.6

from app import create_app
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.extensions.database import db
from app.modules.user.models import User



__author__ = "wind634"

app = create_app('default')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("runserver", Server('0.0.0.0', port=app.config.get('PORT', 9000)))
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app)


if __name__ == "__main__":
    manager.run()
