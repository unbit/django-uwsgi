Integrations
============

Django-Debug-Toolbar
--------------------

If you're using `django-debug-toolbar`_, you can add:

.. code-block:: py

    DEBUG_TOOLBAR_PANELS += ('django_uwsgi.panels.UwsgiPanel',)


.. _django-debug-toolbar: http://django-debug-toolbar.readthedocs.org/en/latest/

.. image:: screenshots/screenshot1.png



Wagtail
-------

If you're using `Wagtail`_:

There is `wagtail_hooks.py` file available and `Wagtail`_ will read it automatically

And you don't have to add `django_uwsgi` into urls.py

`Wagtail`_ admin interface:

.. image:: screenshots/screenshot2.png


.. image:: screenshots/screenshot3.png


.. _Wagtail: http://wagtail.io