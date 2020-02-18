class Config(object):
    DEBUG = False
    TESTING= False

class DevelopmentConfig(Config):
    ENV = 'dev'
    DEBUG = True

class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    FLASK_ENV = 'production'
