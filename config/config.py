from config.dev import DevelopmentConfig
from config.prod import ProductionConfig
from config.test import TestingConfig

config_settings = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}