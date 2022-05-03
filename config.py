import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'english.db')
    SECRET_KEY = os.urandom(32)
    SECRET_KEYS = SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = False
