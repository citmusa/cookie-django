#!/bin/bash
pip install --upgrade pip
pip install -r requirements/development.txt
wget https://github.com/twbs/bootstrap/archive/v{{ cookiecutter.bootstrap_version }}.tar.gz
tar -xzf v{{ cookiecutter.bootstrap_version }}.tar.gz

mv bootstrap-{{ cookiecutter.bootstrap_version }}/dist/js/bootstrap.min.js {{ cookiecutter.project_slug }}/static/js/
mv bootstrap-{{ cookiecutter.bootstrap_version }}/dist/fonts/* {{ cookiecutter.project_slug}}/static/fonts/
mv bootstrap-{{ cookiecutter.bootstrap_version }}/dist/css/bootstrap.css {{ cookiecutter.project_slug }}/static/css/
rm v{{ cookiecutter.bootstrap_version }}.tar.gz
rm -rf bootstrap-{{ cookiecutter.bootstrap_version }}

wget -O  {{cookiecutter.project_slug }}/static/js/jquery.min.js https://code.jquery.com/jquery-{{ cookiecutter.jquery_version}}.min.js
cd {{cookiecutter.project_slug }}
# todo: add git init
