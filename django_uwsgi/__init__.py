__version__ = '17.6.2'


try:
    import uwsgi
except ImportError:
    uwsgi = None

try:
    from six.moves import cPickle as pickle
except ImportError:
    import pickle

default_app_config = 'django_uwsgi.apps.DjangoUwsgiConfig'
