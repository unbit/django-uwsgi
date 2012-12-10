from django.conf.urls import patterns, url

urlpatterns = patterns('uwsgi_admin.views',
    url(r'^$', 'index', name='uwsgi_index'),
    url(r'^reload/$', 'reload', name='uwsgi_reload')
)
