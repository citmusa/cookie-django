# coding: utf-8
from common import *
import raven

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['{{ cookiecutter.project_domain }}']

{% if cookiecutter.database == 'Mysql' %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{ cookiecutter.project_slug }}_db',
        'HOST': '0.0.0.0',
        'USER': '{{ cookiecutter.project_slug }}_usr',
        'PASSWORD': 'NotSet'
    }
}
{% elif cookiecutter.database == 'postgresql' %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ cookiecutter.project_slug }}_db',
        'HOST': '0.0.0.0',
        'USER': '{{ cookiecutter.project_slug }}_usr',
        'PASSWORD': 'NotSet'
    }
}
{% else %}
# DATABASES = {
#     'default': {
#         'ENGINE': '',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': ''
#     }
# }
{% endif %}

# Sentry settings

INSTALLED_APPS.append('raven.contrib.django.raven_compat')
RAVEN_CONFIG = {
    'dsn': 'Unknown',
    'release': raven.fetch_git_sha(
        os.path.dirname(os.path.join(BASE_DIR, '../'))
    ),
    'site': '{{ cookiecutter.project_domain }}',
}

# Custom project settings
# ------------------------------------------------------------------------------
