## django-uwsgi

Django related examples/tricks/modules for uWSGI

### Warning!

 This code is not production ready yet!


### Installation

  ```sh
  pip install django-uwsgi
  ```
  By default django-uwsgi doesn't install uWSGI in case if project deployed in [Emperor](http://uwsgi-docs.readthedocs.org/en/latest/Emperor.html) mode and uWSGI installed system-wide.
  You can install django-uwsgi with uWSGI by adding [uwsgi] to the command:
  ```sh
  pip install django-uwsgi[uwsgi]
  ```

### Setup/Configuration

  Add django_uwsgi into INSTALLED_APPS:
  ```python
  INSTALLED_APPS += ('django_uwsgi',)
  ```
  Add django_uwsgi into urls.py:
  ```python
  urlpatterns += patterns('', url(r'^admin/uwsgi/', include('django_uwsgi.urls')),)
  ```
  If you using [django-debug-toolbar](http://django-debug-toolbar.readthedocs.org/en/latest/), you can add:
  ```python
  DEBUG_TOOLBAR_PANELS += ('django_uwsgi.panels.uWSGIPanel',)
  ```

### Features

  * Admin page with stats (options to reload/stop uWSGI, clear uWSGI cache)
  * uWSGI Cache backend for Django
  * uWSGI Email backend for Django(send emails via uwsgi [spooler](http://uwsgi-docs.readthedocs.org/en/latest/Spooler.html)
  * Debug Panel for [django-debug-toolbar](http://django-debug-toolbar.readthedocs.org/en/latest/panels.html)
  * Django template loader for [embedded](http://uwsgi-docs.readthedocs.org/en/latest/Embed.html) into uWSGI files
  * Django management command runuwsgi(with live autoreload when DEBUG is True)
  * uWSGI config generator

  Some features are not added into repo yet.

### Todo

 * Tests
 * Docs
 * Translations?
 * Screenshots
 * Add Django models to store Vassals info/config in [PostgreSQL](http://uwsgi-docs.readthedocs.org/en/latest/ImperialMonitors.html#pg-scan-a-postgresql-table-for-configuration) or [MongoDB](http://uwsgi-docs.readthedocs.org/en/latest/ImperialMonitors.html#mongodb-scan-mongodb-collections-for-configuration)

### Authors

See [CONTRIBUTORS](CONTRIBUTORS)

### License

[MIT](LICENSE)
