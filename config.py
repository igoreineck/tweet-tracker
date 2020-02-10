class Config(object):
    DEBUG = False
    TESTING= False

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

class TestingConfig(Config):
    TESTING = True