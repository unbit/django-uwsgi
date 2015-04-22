from django.core.management.base import BaseCommand
from django.conf import settings
from django.apps import apps
import os
import sys
import multiprocessing

root = os.getcwd()
django_project = os.path.basename(root)


class Command(BaseCommand):
    help = "Runs this project as a uWSGI application. Requires the uwsgi binary in system path."

    http_port = os.getenv('PORT', '8000')  # for heroku
    socket_addr = None

    def handle(self, *args, **options):
        for arg in args:
            k, v = arg.split('=')
            if k == 'http':
                if self.http_port:
                    self.http_port = v
            elif k == 'socket':
                self.http_port = None
                self.socket_addr = v

        # load the Django WSGI handler
        os.environ['UWSGI_MODULE'] = '%s.wsgi' % django_project
        # DJANGO settings
        if options['settings']:
            os.environ['DJANGO_SETTINGS_MODULE'] = options['settings']
        else:
            os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings' % django_project

        # set protocol as uwsgi
        os.environ['UWSGI_PROTOCOL'] = 'uwsgi'

        # bind the http server to the default port
        if self.http_port:
            os.environ['UWSGI_HTTP_SOCKET'] = ':%s' % self.http_port
        elif self.socket_addr:
            os.environ['UWSGI_UWSGI_SOCKET'] = self.socket_addr
            os.environ['UWSGI_CHMOD_SOCKET'] = '664'
        # set process names
        os.environ['UWSGI_AUTO_PROCNAME'] = 'true'
        os.environ['UWSGI_PROCNAME_PREFIX_SPACED'] = '[uWSGI %s]' % django_project
        # remove sockets/pidfile at exit
        os.environ['UWSGI_VACUUM'] = 'true'
        # retrieve/set the PythonHome
        os.environ['UWSGI_VIRTUALENV'] = sys.prefix
        # add project to python path
        os.environ['UWSGI_PP'] = root

        os.environ['UWSGI_POST_BUFFERING'] = '1048576'
        os.environ['UWSGI_RELOAD_ON_RSS'] = '300'
        # increase buffer size a bit
        os.environ['UWSGI_BUFFER_SIZE'] = '65535'
        # some additions required by newrelic
        os.environ['UWSGI_ENABLE_THREADS'] = 'true'
        os.environ['UWSGI_LAZY_APPS'] = 'true'
        os.environ['UWSGI_SINGLE_INTERPRETER'] = 'true'
        os.environ['UWSGI_AUTOLOAD'] = 'true'
        # set 12 workers and cheaper to number of cpus
        os.environ['UWSGI_WORKERS'] = '12'
        os.environ['UWSGI_CHEAPER'] = str(multiprocessing.cpu_count())
        # enable the master process
        os.environ['UWSGI_MASTER'] = 'true'

        os.environ['UWSGI_NO_ORPHANS'] = 'true'
        os.environ['UWSGI_MEMORY_REPORT'] = 'true'
        os.environ['UWSGI_DISABLE_LOGGING'] = 'true'

        # set harakiri
        os.environ['UWSGI_HARAKIRI'] = '60'
        os.environ['UWSGI_HARAKIRI_VERBOSE'] = 'true'

        # set uid and gid
        os.environ['UWSGI_UID'] = str(os.getuid())
        os.environ['UWSGI_GID'] = str(os.getgid())
        # TODO: Figure out cache
        os.environ['UWSGI_CACHE2'] = 'name=%s,items=20000,keysize=128,blocksize=4096' % django_project
        if settings.DEBUG:
            if apps.is_installed('configurations'):
                os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')
                import configurations
                configurations.setup()
            # map and serve static files
            os.environ['UWSGI_STATIC_MAP'] = '%s=%s' % (settings.STATIC_URL, settings.STATIC_ROOT)
            os.environ['UWSGI_PY_AUTORELOAD'] = '2'
        # run spooler for mail task
        if 'django_uwsgi' in settings.EMAIL_BACKEND:
            os.environ['UWSGI_SPOOLER'] = '/tmp'
            os.environ['UWSGI_SPOOLER_IMPORT'] = 'django_uwsgi.task'
        # exec the uwsgi binary
        if apps.ready:
            os.execvp('uwsgi', ('uwsgi',))


    def usage(self, subcomand):
        return r"""
  run this project on the uWSGI server
  http=PORT run the embedded http server on port PORT
  socket=ADDR bind the uwsgi server on address ADDR (this will disable the http server)
        """
