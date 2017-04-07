import os

from flask_uploads import IMAGES, DOCUMENTS

from config.common import Config, basedir


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


    # ===== 上传相关配置 start =====
    UPLOADS_DEFAULT_DEST = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "uploads")
    UPLOADED_PHOTO_DEST = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "uploads", "photos")
    UPLOADED_PHOTO_ALLOW = IMAGES
    UPLOADED_PHOTO_DENY = DOCUMENTS
    # ===== 上传相关配置 end =====