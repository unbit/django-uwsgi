from django.core.mail import get_connection
from django.conf import settings

from .decorators import spoolforever
from . import pickle
from django.apps import apps

if apps.ready and apps.is_installed('configurations'):
    from configurations import importer
    importer.install()


BACKEND = getattr(settings, 'UWSGI_EMAIL_BACKEND',
                  'django.core.mail.backends.console.EmailBackend')


@spoolforever
def send_mail(arguments):
    conn = get_connection(backend=BACKEND)
    conn.send_messages([pickle.loads(arguments['body'])])
