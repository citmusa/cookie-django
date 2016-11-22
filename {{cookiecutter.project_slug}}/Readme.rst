{{cookiecutter.project_name}}
{{ '=' * cookiecutter.project_name|length }}

{{cookiecutter.description}}


    * django-compressor
    * boostrap {{ cookiecutter.bootstrap_version }}

{% if cookiecutter.database == "MySql" %}
    * Mysql
{% elif cookiecutter.database == "Postgresql" %}
    * Postgresl
{% endif %}
