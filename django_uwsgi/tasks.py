from __future__ import unicode_literals
from django.core.mail import get_connection
from django.conf import settings

from .decorators import spool
from . import pickle


BACKEND = getattr(settings, 'UWSGI_EMAIL_BACKEND',
                  'django.core.mail.backends.smtp.EmailBackend')


@spool
def send_mail(arguments):
    conn = get_connection(backend=BACKEND)
    conn.send_messages([pickle.loads(arguments['body'])])
