import os
import django_heroku
from configparser import RawConfigParser


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = RawConfigParser()
config.read(os.path.join(BASE_DIR, 'config.ini'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

DEBUG = config.getboolean("global", "DEBUG")
SECRET_KEY = config.get('secrets', 'SECRET_KEY')
ALLOWED_HOSTS = []

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'railsprojectteam@gmail.com'
EMAIL_HOST_PASSWORD = 'Salma1234'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


INSTALLED_APPS = [ 
    'projects',
    'users',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'django_seed',
    'django_countries'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crowdfunding.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'crowdfunding.wsgi.application'


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


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# To use our new Model in Authentication
AUTH_USER_MODEL = 'users.UserModel'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')
MEDIA_URL = '/uploads/'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = 'home'

# resset password by gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'test@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'crowdfunding40@gmail.com'
EMAIL_HOST_PASSWORD = 'eivnezduqnzjbvsf'
EMAIL_PORT = 587


# Activate Django-Heroku.
django_heroku.settings(locals())
