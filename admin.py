import os
import pkg_resources

from abu.admin import Interface


class Admin(Interface):
    def version(self):
        return '0.0.1'

    def init(self, path):
        with open(os.path.join(path, 'README'), 'w') as readme:
            readme.write("abc")