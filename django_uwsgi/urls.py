from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.UwsgiStatus.as_view(), name='uwsgi_index'),
    url(r'^reload/$', views.UwsgiReload.as_view(), name='uwsgi_reload'),
    url(r'^cache_clear/$', views.UwsgiCacheClear.as_view(), name='uwsgi_cache_clear'),
    url(r'^log/$', views.UwsgiLog.as_view(), name='uwsgi_log'),
    url(r'^signal/$', views.UwsgiSignal.as_view(), name='uwsgi_signal'),
]
