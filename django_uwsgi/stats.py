import os
import time
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from . import uwsgi


def get_uwsgi_stats():
    uwsgi_stats = {}
    workers = uwsgi.workers()
    total_load = time.time() - uwsgi.started_on
    for w in workers:
        w['running_time'] = w['running_time'] / 1000
        w['avg_rt'] = w['avg_rt'] / 1000
        w['load'] = w['running_time'] / total_load / 10 / len(workers)
        w['last_spawn'] = datetime.fromtimestamp(w['last_spawn'])
    jobs = []
    if uwsgi.opt.get('spooler'):
        spooler_jobs = uwsgi.spooler_jobs()
        for j in spooler_jobs:
            jobs.append({'file': j, 'env': uwsgi.parsefile(str(j))})
    uwsgi_stats.update({
        'uwsgi': uwsgi,
        'stats': [
            ('loop', uwsgi.loop),
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
            ('spooler_pid', uwsgi.spooler_pid() if uwsgi.opt.get('spooler') else _('disabled')),
            ('threads', _('enabled') if uwsgi.has_threads else _('disabled'))
        ],
        'workers': workers,
        'jobs': jobs
    })
    return uwsgi_stats
