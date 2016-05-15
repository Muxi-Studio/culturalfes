# coding: utf-8

# config

# project base path
import os
basedir = os.path.abspath(os.path.dirname(__file__))

"""
common configuration
 -- SECRET_KEY: secret key
 -- SQLALCHEMY_COMMIT_ON_TEARDOWN: True

 -- SQLALCHEMY_RECORD_QUERIES:
    -- Can be used to explicitly disable or enable query recording.
       Query recording automatically happens in debug or testing mode.

 -- SQLALCHEMY_TRACK_MODIFICATIONS:
    -- If set to True, Flask-SQLAlchemy will track modifications of
       objects and emit signals.
       The default is None, which enables tracking but issues a warning that
       it will be disabled by default in the future.
       This requires extra memory and should be disabled if not needed.

 more configuration keys please see:
  -- http://flask-sqlalchemy.pocoo.org/2.1/config/#configuration-keys
"""
class Config:
    """common configuration"""
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif', 'rar']
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    BUPLOAD_FOLDER = os.environ.get('BUPLOAD_FOLDER')
    REDIS_URL = "redis://:password@localhost:6379/0"
    CAPTCHA_ID = "b46d1900d0a894591916ea94ea91bd2c"
    PRIVATE_KEY = "36fc3fe98530eea08dfc6ce76e3d24c4"

    @staticmethod
    def init_app(app):
        pass

"""
development configuration
 -- DEBUG: debug mode
 -- SQLALCHEMY_DATABASE_URI:
    -- The database URI that should be used for the connection.

more connection URI format:
 -- Postgres:
    -- postgresql://scott:tiger@localhost/mydatabase
 -- MySQL:
    -- mysql://scott:tiger@localhost/mydatabase
 -- Oracle:
    -- oracle://scott:tiger@127.0.0.1:1521/sidname
"""
class DevelopmentConfig(Config):
    """development configuration"""
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")
    SQLALCHEMY_DATABASE_URI =  os.environ.get('MYSQL_URI')

"""
testing configuration
 -- TESTING: True
 -- WTF_CSRF_ENABLED:
    -- in testing environment, we don't need CSRF enabled
"""
class TestingConfig(Config):
    """testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data-test.sqlite")
    WTF_CSRF_ENABLED = False

# production configuration
class ProductionConfig(Config):
    """production configuration"""
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.sqlite")
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    "develop": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}

