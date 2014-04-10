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
### Upcoming Features

  * Admin page with stats (with options to reload uWSGI, clear uWSGI cache)
  * uWSGI Cache backend for Django
  * uWSGI Email backend for Django(send emails via uwsgi [spooler](http://uwsgi-docs.readthedocs.org/en/latest/Spooler.html)
  * Debug Panel for [django-debug-toolbar](http://django-debug-toolbar.readthedocs.org/en/latest/panels.html)
  * Django template loader for [embedded](http://uwsgi-docs.readthedocs.org/en/latest/Embed.html) into uWSGI files
  * Django management command runuwsgi
  * uWSGI config generator
  * Live autoreload when DEBUG is True

  Some features are not added into repo yet.

### Todo

 * Tests
 * Docs
 * Translations?
 * Screenshots

### Authors

See [CONTRIBUTORS](CONTRIBUTORS)

### License

[MIT](LICENSE)
