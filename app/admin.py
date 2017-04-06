import os
import pkg_resources

from abu.admin import Interface


class Admin(Interface):
    def version(self):
        return '0.0.1'

    def init(self, path):
        print("init...")

    def backup(self, path, backup_file):
        print("backup...")

    def restore(self, path, restore_file):
        print("restore...")

    def upgrade(self, path, old_version):
        print("upgrade...")