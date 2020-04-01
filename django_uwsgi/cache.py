try:
    from django.utils.encoding import force_bytes as stringify
except ImportError:
    from django.utils.encoding import smart_str as stringify
from django.core.cache.backends.base import BaseCache, InvalidCacheBackendError
from django.conf import settings


try:
    from . import uwsgi, pickle
except ImportError:
    if getattr(settings, "UWSGI_CACHE_FALLBACK", True):
        uwsgi = None
    else:
        raise InvalidCacheBackendError(
            "You're not running under uWSGI ! "
            "Set UWSGI_CACHE_FALLBACK=True in settings if you want to fallback "
            "to LocMemCache."
        )


if uwsgi:
    class UwsgiCache(BaseCache):
        """uWSGI cache backend"""
        def __init__(self, server, params):
            BaseCache.__init__(self, params)
            self._cache = uwsgi
            self._server = server

        def exists(self, key):
            return self._cache.cache_exists(stringify(key), self._server)

        def add(self, key, value, timeout=True, version=None):
            full_key = self.make_key(key, version=version)
            if self.exists(full_key):
                return False
            self._set(full_key, value, timeout)
            return True

        def get(self, key, default=None, version=None):
            full_key = self.make_key(key, version=version)
            val = self._cache.cache_get(stringify(full_key), self._server)
            if val is None:
                return default
            val = stringify(val)
            return pickle.loads(val)

        def _set(self, full_key, value, timeout):
            if timeout is True:
                uwsgi_timeout = self.default_timeout
            elif timeout is None or timeout is False:
                # Django 1.6+: Explicitly passing in timeout=None will set a non-expiring timeout.
                uwsgi_timeout = 0
            elif timeout == 0:
                # Django 1.6+: Passing in timeout=0 will set-and-expire-immediately the value.
                uwsgi_timeout = -1
            else:
                uwsgi_timeout = timeout
            self._cache.cache_update(stringify(full_key), pickle.dumps(value), uwsgi_timeout, self._server)

        def set(self, key, value, timeout=True, version=None):
            full_key = self.make_key(key, version=version)
            self._set(full_key, value, timeout)

        def delete(self, key, version=None):
            full_key = self.make_key(key, version=version)
            self._cache.cache_del(stringify(full_key), self._server)

        def close(self, **kwargs):
            pass

        def clear(self):
            self._cache.cache_clear(self._server)
else:
    from django.core.cache.backends.locmem import LocMemCache as UwsgiCache
