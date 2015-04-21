Adding Django-uWSGI to your project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add ``'django_uwsgi',`` to your ``INSTALLED_APPS`` in ``settings.py``:

.. code-block:: py

   INSTALLED_APPS += ('django_uwsgi',)


Add django_uwsgi into ``urls.py``:

.. code-block:: py

   urlpatterns += patterns('', url(r'^admin/uwsgi/', include('django_uwsgi.urls')),)


If you're using `django-debug-toolbar`_, you can add:

.. code-block:: py

   DEBUG_TOOLBAR_PANELS += ('django_uwsgi.panels.uWSGIPanel',)


.. _django-debug-toolbar: http://django-debug-toolbar.readthedocs.org/en/latest/