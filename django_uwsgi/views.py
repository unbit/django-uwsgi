import os
import time
from datetime import datetime
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, TemplateView
from django_uwsgi import uwsgi


class uWSGIStatus(TemplateView):

    """uWSGI Status View"""

    template_name = 'uwsgi/uwsgi.html'

    def get_context_data(self, **kwargs):
        context = super(uWSGIStatus, self).get_context_data(**kwargs)
        if uwsgi is None:
            context['unavailable'] = True
            return context
        else:
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

            context.update({
                'version': uwsgi.version,
                'hostname': uwsgi.hostname,
                'os': os.uname(),
                'masterpid': uwsgi.masterpid(),
                'stats': [
                    ('masterpid', str(uwsgi.masterpid())),
                    ('started_on', datetime.fromtimestamp(uwsgi.started_on)),
                    ('now', datetime.now()),
                    ('buffer_size', uwsgi.buffer_size),
                    ('total_requests', uwsgi.total_requests()),
                    ('numproc', uwsgi.numproc),
                    ('cores', uwsgi.cores),
                    ('cwd', os.getcwd()),
                    ('logsize', uwsgi.logsize()),
                    ('cache_exists', uwsgi.cache_exists),
                    ('spooler_pid', uwsgi.spooler_pid()
                     if uwsgi.opt.get('spooler') else 'disabled'),
                    ('threads', 'enabled' if uwsgi.has_threads else 'disabled')
                ],
                'options': uwsgi.opt.items(),
                'workers': workers,
                'jobs': jobs,
            })
            return context


class uWSGICacheClear(View):

    """Clear uWSGI Cache View"""

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        if uwsgi is not None and uwsgi.masterpid() > 0:
            uwsgi.cache_clear()
            messages.add_message(request, messages.SUCCESS, _(
                'uWSGI Cache cleared!'), fail_silently=True)
        else:
            messages.add_message(request, messages.ERROR, _(
                'The uWSGI master process is not active'), fail_silently=True)
        return HttpResponseRedirect(reverse_lazy('uwsgi_index'))


class uWSGIReload(View):

    """Reload uWSGI View"""

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        if uwsgi is not None and uwsgi.masterpid() > 0:
            uwsgi.reload()
            messages.add_message(
                request, messages.SUCCESS, _('uWSGI reloaded!'), fail_silently=True)
        else:
            messages.add_message(request, messages.ERROR, _(
                'The uWSGI master process is not active'), fail_silently=True)
        return HttpResponseRedirect(reverse_lazy('uwsgi_index'))
