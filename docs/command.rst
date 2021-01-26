Management Command
==================

runuwsgi
--------

.. code-block:: sh

   python manage.py runuwsgi

runuwsgi options:
-----------------

http
----

.. code-block:: sh

   python manage.py runuwsgi http=8000


socket
------

.. code-block:: sh

   python manage.py runuwsgi socket=/tmp/projectname-uwsgi.sock

Other options
-------------

Any other options can be passed via environment variables, prefixed with `UWSGI_` and converted
to upper-case, or as key-value pairs in a dictionary named `UWSGI` in settings.

Options from `UWSGI` in settings are passed to uwsgi as INI, which allows passing multi-value
options. Example:

.. code-block:: python

   UWSGI = {
       "module": "my.project.wsgi",
       "attach-daemon": ["memcached -p 11311", "celery -A my.project.tasks worker"]
   }
