Email Backend
=============

A Django backend for e-mail delivery using uWSGI Spool to queue deliveries.

Usage
-----

First, add uWSGI backend in your settings file.


.. code-block:: py

    EMAIL_BACKEND = 'django_uwsgi.mail.EmailBackend'


And send your e-mails normally.


.. code-block:: py

    from django.core.mail import send_mail

    send_mail('Subject here', 'Here is the message.', 'from@example.com',
        ['to@example.com'], fail_silently=False)


Note
----

You must setup uwsgi spooler.
Example ini:


.. code-block:: ini

    plugin = spooler
    spooler = /tmp
    spooler-import = django_uwsgi.task


or use built in management command `runuwsgi`


Changing the backend
--------------------

By default the 'django.core.mail.backends.smtp.EmailBackend' is used for the real e-mail delivery. You can change that using: 

.. code-block:: py

    UWSGI_EMAIL_BACKEND = 'your.backend.EmailBackend'


django-configurations
---------------------

If you're using django-configurations in your project, you must setup importer as mentioned in django-configurations docs for celery