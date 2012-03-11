import os
import sys


SAWHORSE_HOME = os.environ['SAWHORSE_HOME']
APP_NAME = os.environ['SAWHORSE_APP']
APP_ROOT = os.path.join(SAWHORSE_HOME, APP_NAME)


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(APP_ROOT, 'sqlite.db'),
    }
}

SITE_ID = 1
SECRET_KEY = ' '

MEDIA_ROOT = os.path.join(APP_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(APP_ROOT, 'static')
STATIC_URL = '/static/'

ROOT_URLCONF = 'sawhorse.urls'

TEMPLATE_DIRS = [os.path.join(SAWHORSE_HOME, 'templates')]


sys.path.insert(0, '')

try:
    from required_settings import *
except ImportError:
    pass

try:
    from local_settings import *
except ImportError:
    pass


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
] + INSTALLED_APPS
