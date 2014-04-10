from django.conf.urls import patterns, url
from django_uwsgi.views import uWSGIReload, uWSGIStatus, uWSGICacheClear

urlpatterns = patterns('',
    url(r'^$', uWSGIStatus.as_view(), name='uwsgi_index'),
    url(r'^reload/$', uWSGIReload.as_view(), name='uwsgi_reload'),
    url(r'^clear_cache/$', uWSGICacheClear.as_view(), name='uwsgi_cache_clear'),
)
