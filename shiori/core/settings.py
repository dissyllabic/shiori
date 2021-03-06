# -*- coding: utf-8 -*-
"""
Django settings for shiori project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from __future__ import absolute_import

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Don't forget to replace me!
SECRET_KEY = 'secret key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_openid_auth',
    'south',
    'shiori.bookmark',
    'shiori.api',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'shiori.core.urls'

WSGI_APPLICATION = 'shiori.core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS': ('rest_framework.serializers.'
                                       'HyperlinkedModelSerializer'),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        ),
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.DjangoModelPermissions',
        # 'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAdminUser',
        ],
    'PAGINATE_BY': 20}


OPENID_CREATE_USERS = True
OPENID_UPDATE_DETAILS_FROM_SREG = True
LOGIN_URL = '/openid/login/'
LOGIN_REDIRECT_URL = '/shiori'
OPENID_USE_AS_ADMIN_LOGIN = False
OPENID_STRICT_USERNAMES = True
OPENID_USE_EMAIL_FOR_USERNAME = True


# Modify temporarily the session serializer because the json serializer in
# Django 1.6 can't serialize openid.yadis.manager.YadisServiceManager objects
# http://bazaar.launchpad.net/~strycore/django-openid-auth/trunk/revision/115
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

BROKER_URL = 'amqp://guest:guest@localhost//'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_TIMEDELTA_MINUTES = 60


# loopback addresses have been excluded in default.
FEED_EXCLUDE_FQDN = (
    # 'shiori.example.org',
)
