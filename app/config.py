"""
Happy Cobra - Marirs
Skeleton of a Login & Registration system
MIT License
"""
import os


def check_dirs_if_exists(*args):
    """Validate the given directories exists.
    If the given directories do not exist, then creates them.
    :param args: dir1, dir2, dir3, etc, ...
    :return: None. (creates directories if they do not exist)
    """
    for arg in args:
        if not os.access(arg, os.F_OK):
            print("{} does not exist; creating...".format(arg))
            os.makedirs(arg)


class Config(object):
    """Common Config
    """
    DEBUG = True
    DATABASE_URI = 'sqlite:///:memory:'

    SECRET_KEY = 'r+)mr^G(:BJ:V-/o1@?aN2ryxd&~0t'
    SECURITY_PASSWORD_SALT = 'A33q8RPeTQz6QcveOPeiwzBP_FCEvBckvENPHeKtj5rhRThNf5E6w188CIwD'
    APP_STATIC_FOLDER = os.path.join(os.getcwd(), 'app', 'static')

    SECURITY_RECOVERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'

    SECURITY_CONFIRM_EMAIL_WITHIN = '1 days'
    SECURITY_RESET_PASSWORD_WITHIN = '1 days'

    SECURITY_LOGIN_URL = '/account_login'
    SECURITY_LOGOUT_URL = '/account_logout'
    SECURITY_RESET_URL = '/account_reset'
    SECURITY_CHANGE_URL = '/account_change'
    SECURITY_CONFIRM_URL = '/confirm_account'
    # SECURITY_POST_LOGIN_VIEW = '/index'
    # SECURITY_POST_LOGOUT_VIEW = '/index'
    # SECURITY_POST_REGISTER_VIEW = '/index'
    # SECURITY_POST_CONFIRM_VIEW = '/index'
    # SECURITY_POST_RESET_VIEW = '/index'
    # SECURITY_POST_CHANGE_VIEW = '/index'
    # SECURITY_UNAUTHORIZED_VIEW = '/index'
    SECURITY_REGISTER_URL = '/signup'
    SECURITY_REGISTER_USER_TEMPLATE = 'security/register.html'
    SECURITY_EMAIL_SENDER = ''


class ProductionConfig(Config):
    """Production Config
    """
    DEBUG = False
    TEMPLATES_AUTO_RELOAD = False
    EXPLAIN_TEMPLATE_LOADING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = ''

    MAIL_SERVER = 'localhost'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_DEFAULT_SENDER = 'noreply@'
    MAIL_PASSWORD = ''


class DevelopmentConfig(Config):
    """Development Config
    """
    DEBUG = True
    JSONIFY_PRETTYPRINT_REGULAR = True
    TEMPLATES_AUTO_RELOAD = True
    EXPLAIN_TEMPLATE_LOADING = True
    DB_PATH = os.path.join(os.getcwd(), 'app', 'db')
    check_dirs_if_exists(DB_PATH)

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_PATH + '/app.db'

    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'apikey'
    MAIL_DEFAULT_SENDER = 'registration_confirmation'
    MAIL_PASSWORD = ''
