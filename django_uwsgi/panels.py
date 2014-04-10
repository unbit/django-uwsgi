from debug_toolbar.panels import DebugPanel
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
import uwsgi
import time


class uWSGIDebugPanel(DebugPanel):
    name = 'uWSGI'
    has_content = True

    def nav_title(self):
        return _('uWSGI')

    def title(self):
        return _('uWSGI status')

    def url(self):
        return ''

    def content(self):
        workers = uwsgi.workers()
        total_load = time.time() - uwsgi.started_on
        for w in workers:
            w['load'] = (100 * (w['running_time'] / 1000)) / total_load
            w['last_spawn_str'] = time.ctime(w['last_spawn'])

        jobs = []
        if 'spooler' in uwsgi.opt:
            spooler_jobs = uwsgi.spooler_jobs()
            for j in spooler_jobs:
                jobs.append({'file': j, 'env': uwsgi.parsefile(j)})
        context = self.context.copy()
        context.update({'masterpid': uwsgi.masterpid(),
                        'started_on': time.ctime(uwsgi.started_on),
                        'buffer_size': uwsgi.buffer_size,
                        'total_requests': uwsgi.total_requests(),
                        'numproc': uwsgi.numproc,
                        'workers': workers,
                        'jobs': jobs,
                        })
        return render_to_string('uwsgi_admin/uwsgi_panel.html', context)
