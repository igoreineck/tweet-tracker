class Config(object):
    DEBUG = False
    TESTING= False

class DevelopmentConfig(Config):
    ENV = 'dev'
    DEBUG = True

class TestingConfig(Config):
    ENV = 'testing'
    TESTING = True
    DEBUG = True