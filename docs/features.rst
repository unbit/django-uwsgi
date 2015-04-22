Features
========

* Admin page with `uWSGI`_ stats (options to reload/stop uWSGI, clear uWSGI cache)
* uWSGI :doc:`cache` for Django
* uWSGI :doc:`email` for Django(send emails via uWSGI's `spooler`_)
* Debug Panel for `django-debug-toolbar`_ (offers same functions as admin page)
* Django template loader for `embedded`_ into uWSGI files
* Django :doc:`command` ``runuwsgi`` (with live autoreload when DEBUG is True)
* uWSGI config generator
* Django CBV Mixins based on uWSGI decorators

Some features are not added into repo or not yet implemented(See :doc:`todo`)


.. _uWSGI: http://uwsgi-docs.readthedocs.org/en/latest/
.. _django-debug-toolbar: http://django-debug-toolbar.readthedocs.org/en/latest/
.. _spooler: http://uwsgi-docs.readthedocs.org/en/latest/Spooler.html
.. _embedded: http://uwsgi-docs.readthedocs.org/en/latest/Embed.html