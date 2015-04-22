from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.UwsgiStatus.as_view(), name='uwsgi_index'),
    url(r'^reload/$', views.UwsgiReload.as_view(), name='uwsgi_reload'),
    url(r'^clear_cache/$', views.UwsgiCacheClear.as_view(), name='uwsgi_cache_clear'),
)
