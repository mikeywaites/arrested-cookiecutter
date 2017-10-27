import os


class Config(object):

    pass


class Dev(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////opt/code/{{cookiecutter.package_name}}.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASIC_AUTH_USERNAME = 'admin'
    BASIC_AUTH_PASSWORD = 'secret'


settings = globals()[os.environ.get('FLASK_CONFIG', 'Dev')]
