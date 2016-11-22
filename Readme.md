## Django bootstrap project template
### Includes
* Twitter bootstrap 3
* django-annoying
* django-compressor

### How to use
Create virtual environment, change project_name with your projects name :D
```sh
mkvirtualenv project_name
```

Install cookiecutter
```sh
pip install cookiecutter
```

Run cookiecutter
```sh
cookiecutter -this.repo.git-
```

You'll be prompted for some questions, answer them, then it will create a Django project for you.

Install requirements, for development
```sh
pip install -r requirements/development.txt
```

Set 'PROJECT_ENV' environment variable.
* 'development'
* 'production',
* 'staging'

If no 'PROJECT_ENV' especified takes 'development' settings as default

For development environment:
```sh
sudo sh -c 'echo "export PROJECT_ENV=development" >> /etc/profile.d/environment.sh' && source /etc/profile.d/environment.sh
```
Done.
