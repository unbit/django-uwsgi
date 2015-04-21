from django.core.mail.backends.base import BaseEmailBackend
from . import pickle


class EmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        num_sent = 0
        if not email_messages:
            return
        for email_message in email_messages:
            if self._send(email_message):
                num_sent += 1
        return num_sent

    def _send(self, email_message):
        from .task import send_mail
        send_mail.spool(body=pickle.dumps(email_message, 2))
        return True