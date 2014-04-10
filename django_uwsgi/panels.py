"""uWSGI Debug Toolbar Panel"""

from debug_toolbar.panels import Panel
from django.utils.translation import ugettext_lazy as _
import time
from datetime import datetime
from django_uwsgi import uwsgi


class uWSGIPanel(Panel):
    """uWSGI Debug Toolbar Panel"""

    title = _('uWSGI Status')
    nav_title = _('uWSGI Status')
    template = 'uwsgi/panel.html'

    @property
    def nav_subtitle(self):
        if uwsgi is not None:
            status = 'Version %s, %d Processes' % (
                uwsgi.version, uwsgi.numproc)
        else:
            status = _('uWSGI is missing =(')
        return status

    def process_response(self, request, response):
        if uwsgi is not None:
            workers = uwsgi.workers()
            total_load = time.time() - uwsgi.started_on
            for w in workers:
                w['running_time'] = w['running_time'] / 1000
                w['load'] = w['running_time'] / total_load / 10 / len(workers)
                w['last_spawn'] = datetime.fromtimestamp(w['last_spawn'])

            jobs = []
            if 'spooler' in uwsgi.opt:
                spooler_jobs = uwsgi.spooler_jobs()
                for j in spooler_jobs:
                    jobs.append({'file': j, 'env': uwsgi.parsefile(j)})
            self.record_stats({
                'version': uwsgi.version,
                'hostname': uwsgi.hostname,
                'masterpid': uwsgi.masterpid(),
                'stats': [
                    ('masterpid', str(uwsgi.masterpid())),
                    ('started_on', datetime.fromtimestamp(uwsgi.started_on)),
                    ('now', datetime.now()),
                    ('buffer_size', uwsgi.buffer_size),
                    ('total_requests', uwsgi.total_requests()),
                    ('numproc', uwsgi.numproc),
                    ('cores', uwsgi.cores),
                    ('spooler pid', uwsgi.spooler_pid()
                     if uwsgi.opt.get('spooler') else 'disabled'),
                    ('threads', 'enabled' if uwsgi.has_threads else 'disabled')
                ],
                'options': uwsgi.opt.items(),
                'workers': workers,
                'jobs': jobs,
            })
        else:
            self.record_stats({'unavailable': True})
