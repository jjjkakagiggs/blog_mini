import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    ARTICLES_PER_PAGE = 15
    COMMENTS_PER_PAGE = 20
    WTF_CSRF_SECRET_KEY = 'random key for form'  # for csrf protection

    # @staticmethod
    # def init_app(app):
    #     pass


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'blog_mini-dev.db')


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'blog_mini-test.db'))  # in-memory database


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'blog_mini-pro.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}