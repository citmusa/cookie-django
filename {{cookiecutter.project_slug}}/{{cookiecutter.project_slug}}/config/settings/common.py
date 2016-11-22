# coding: utf-8
"""
Django settings for {{ cookiecutter.project_name }} project.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from __future__ import absolute_import, unicode_literals
import os
from unipath import FSPath as Path
from django.utils.translation import ugettext_lazy as _

BASE_DIR = Path(__file__).absolute().parent.parent.parent
SECRET_KEY = '4^-3hj1ufij#7v0ib*=eo@9lyn#84np*3-843f)!36+c3krqua'
ALLOWED_HOSTS = []

DEBUG = False

ADMINS = (
    ('Admin', 'desarrolloqa@comunicaciongm.com.mx'),
)
MANAGERS = ADMINS

# Internationalization
# ------------------------------------------------------------------------------

LANGUAGE_CODE = 'es'
# LANGUAGE_CODE = 'es-mx'  # lower support
LANGUAGES = (
    ('es', _('Spanish')),
)
TIME_ZONE = 'America/Mexico_City'
USE_L10N = True
USE_I18N = True
USE_TZ = True

# App definitions
# ------------------------------------------------------------------------------
WSGI_APPLICATION = 'config.wsgi.application'
SITE_ID = 1

# URL's
# ------------------------------------------------------------------------------
# Location of root django.contrib.admin URL, use {% raw %}{% url 'admin:index' %}{% endraw %}
ROOT_URLCONF = 'config.urls'
ADMIN_URL = r'^djmanager/'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'compressor',
    'utils',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Media and static files settings
# ------------------------------------------------------------------------------
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'utils.context_processors.git',
            ],
        },
    },
]

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)



# Email
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = 'no-reply@project.com.mx'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Database
# ------------------------------------------------------------------------------
# in each environment setting

# Logging
# ------------------------------------------------------------------------------

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "simple": {"format": "[%(name)s] %(levelname)s: %(message)s"},
        "full": {"format": "%(asctime)s [%(name)s] %(levelname)s: %(message)s"},
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ['require_debug_false'],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
    }
}


# Compressor settings
# ------------------------------------------------------------------------------
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
COMPRESS_CSS_HASHING_METHOD = 'content'

# Custom project settings
# ------------------------------------------------------------------------------
