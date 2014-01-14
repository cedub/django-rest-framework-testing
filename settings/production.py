from settings.common import *

# Django settings for motiv8_django project in development.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

WSGI_APPLICATION = 'wsgi.production.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'spbt_demo',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'spbt_demo',
        'PASSWORD': 'SDLKJVXX><M23.,mc!!!slkjewr',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
