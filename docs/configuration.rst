Configuration
=============

Adding django-uwsgi to your project
-----------------------------------

Add ``'django_uwsgi',`` to your ``INSTALLED_APPS`` in ``settings.py``:

.. code-block:: py

    INSTALLED_APPS += ('django_uwsgi',)


Add django_uwsgi into ``urls.py``:

.. code-block:: py

    urlpatterns += patterns('', url(r'^admin/uwsgi/', include('django_uwsgi.urls')),)