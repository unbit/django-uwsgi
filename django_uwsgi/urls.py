from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.UwsgiStatus.as_view(), name='uwsgi_index'),
    url(r'^reload/$', views.UwsgiReload.as_view(), name='uwsgi_reload'),
    url(r'^clear_cache/$', views.UwsgiCacheClear.as_view(), name='uwsgi_cache_clear'),
]
