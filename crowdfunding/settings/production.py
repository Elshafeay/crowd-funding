from crowdfunding.settings.base import *
from distutils.util import strtobool

DEBUG = os.environ.get('DEBUG').lower() == 'true'
SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS').lower() == 'true'
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT'))
COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

MEDIA_LOCATION = "media"
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'

AZURE_ACCOUNT_NAME = "crowdfundingiti"
AZURE_CUSTOM_DOMAIN = f"{AZURE_ACCOUNT_NAME}.blob.core.windows.net"
AZURE_ACCOUNT_KEY = os.environ.get('AZURE_ACCOUNT_KEY')
AZURE_CONTAINER = 'media'

MEDIA_URL = f"https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/"

# Activate Django-Heroku.
django_heroku.settings(locals())
