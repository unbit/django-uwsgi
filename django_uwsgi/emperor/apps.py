from django.apps import AppConfig


class EmperorConfig(AppConfig):
    name = 'django_uwsgi.emperor'
    label = 'uwsgi_emperor'
    verbose_name = 'uWSGI Emperor'

    def ready(self):
        pass# import django_uwsgi.emperor.signals