import os
import sys


SAWHORSE_APP = os.environ['SAWHORSE_APP']
SAWHORSE_ROOT = os.environ['SAWHORSE_ROOT']


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SAWHORSE_ROOT, 'sqlite.db'),
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

SITE_ID = 1
SECRET_KEY = ' '
ROOT_URLCONF = 'sawhorse.urls'

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

MEDIA_ROOT = os.path.join(SAWHORSE_ROOT, 'media')
MEDIA_URL = '/media/'

STATICFILES_FINDERS = ['django.contrib.staticfiles.finders.AppDirectoriesFinder']
STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        }
    }
]

INSTALLED_APPS = [SAWHORSE_APP]


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
