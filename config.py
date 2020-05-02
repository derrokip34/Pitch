import os

class Config():
    SECRET_KEY = 'derrokip34'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://derrick:montolivo@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}