from crowdfunding.settings.base import *
from configparser import RawConfigParser
config = RawConfigParser()
config.read(os.path.join(BASE_DIR, '../config.ini'))


DEBUG = config.getboolean('global', 'DEBUG')
SECRET_KEY = config.get('secrets', 'SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE':   config.get('database', 'DATABASE_ENGINE'),
        'NAME':     config.get('database', 'DATABASE_NAME'),
        'USER':     config.get('database', 'DATABASE_USER'),
        'PASSWORD': config.get('database', 'DATABASE_PASSWORD'),
        'HOST':     config.get('database', 'DATABASE_HOST'),
        'PORT':     config.getint('database', 'DATABASE_PORT'),
    }
}

EMAIL_BACKEND = config.get('email', 'EMAIL_BACKEND')
EMAIL_USE_TLS = config.getboolean('email', 'EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = config.get('email', 'DEFAULT_FROM_EMAIL')
EMAIL_HOST = config.get('email', 'EMAIL_HOST')
EMAIL_HOST_USER = config.get('email', 'EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config.get('email', 'EMAIL_HOST_PASSWORD')
EMAIL_PORT = config.getint('email', 'EMAIL_PORT')
COMPRESS_ENABLED = False
