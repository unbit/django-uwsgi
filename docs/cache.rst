Cache Backend
=============

Installation
------------

change settings to:


.. code-block:: py

    CACHES = {
        'default': {
            'BACKEND': 'django_uwsgi.cache.UwsgiCache',

            # and optionally, if you use a different cache name
            'LOCATION': 'foobar'
        }
    }


Settings
--------

``UWSGI_CACHE_FALLBACK``

- ``False`` - raises Exception if ``uwsgi`` cannot be imported.
- ``True`` (default) - if uwsgi is not importable this cache backend will alias
  to LocMemCache. Note that south or other mangement commands might try to load
  the cache backend so this is why it's the default.