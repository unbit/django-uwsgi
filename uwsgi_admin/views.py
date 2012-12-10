import uwsgi
import time
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages


@staff_member_required
def index(request):
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

    return render_to_response('uwsgi_admin/uwsgi.html', {
        'masterpid': uwsgi.masterpid(),
        'started_on': time.ctime(uwsgi.started_on),
        'buffer_size': uwsgi.buffer_size,
        'total_requests': uwsgi.total_requests(),
        'numproc': uwsgi.numproc,
        'workers': workers,
        'jobs': jobs,
    }, RequestContext(request, {}))


@staff_member_required
def reload(request):
    if uwsgi.masterpid() > 0:
        uwsgi.reload()
        messages.add_message(request,
                             messages.SUCCESS,
                             _('uWSGI reloaded'),
                             fail_silently=True)
    else:
        messages.add_message(request,
                             messages.ERROR,
                             _('The uWSGI master process is not active'),
                             fail_silently=True)

    return HttpResponseRedirect(reverse(index))
