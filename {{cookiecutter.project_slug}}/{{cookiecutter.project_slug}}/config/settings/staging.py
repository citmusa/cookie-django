from common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['{{ cookiecutter.project_slug }}.stagemrm-mccann.com']

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

# Custom project settings
# ------------------------------------------------------------------------------

