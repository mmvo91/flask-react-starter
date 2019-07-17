import os


class DevelopmentConfig(object):
    DEBUG = True

    SECRET_KEY = os.getenv('SECRET_KEY')

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_SESSION_COOKIE = False
    JWT_ACCESS_COOKIE_PATH = '/'
    JWT_REFRESH_COOKIE_PATH = '/'
    JWT_COOKIE_SECURE = False

    SQLALCHEMY_USERNAME = os.getenv('SQLALCHEMY_USERNAME', 'postgres')
    SQLALCHEMY_PASSWORD = os.getenv('SQLALCHEMY_PASSWORD', 'postgres')
    SQLALCHEMY_DB = os.getenv('SQLALCHEMBY_DB', 'postgres')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{SQLALCHEMY_USERNAME}:{SQLALCHEMY_PASSWORD}@localhost:5432/{SQLALCHEMY_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class StagingConfig(DevelopmentConfig):
    DEBUG = False

    SQLALCHEMY_ECHO = False


class ProductionConfig(DevelopmentConfig):
    DEBUG = False

    JWT_COOKIE_SECURE = True

    SQLALCHEMY_ECHO = False


configs = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}

config = configs[os.getenv('FLASK_ENV', 'development')]
