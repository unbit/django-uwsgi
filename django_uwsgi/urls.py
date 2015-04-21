from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.uWSGIStatus.as_view(), name='uwsgi_index'),
    url(r'^reload/$', views.uWSGIReload.as_view(), name='uwsgi_reload'),
    url(r'^clear_cache/$', views.uWSGICacheClear.as_view(), name='uwsgi_cache_clear'),
)