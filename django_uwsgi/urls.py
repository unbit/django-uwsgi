from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', admin.site.admin_view(views.UwsgiStatus.as_view()),
        name='uwsgi_index'),
    url(r'^reload/$', admin.site.admin_view(views.UwsgiReload.as_view()),
        name='uwsgi_reload'),
    url(r'^cache_clear/$', admin.site.admin_view(
        views.UwsgiCacheClear.as_view()), name='uwsgi_cache_clear'),
    url(r'^log/$', admin.site.admin_view(views.UwsgiLog.as_view()),
        name='uwsgi_log'),
    url(r'^signal/$', admin.site.admin_view(views.UwsgiSignal.as_view()),
        name='uwsgi_signal'),
]
