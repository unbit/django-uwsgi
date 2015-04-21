from django.conf import settings
from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore import hooks
from wagtail.wagtailadmin.menu import MenuItem
from wagtail.wagtailadmin.site_summary import SummaryItem
from . import uwsgi, views, urls



class uWSGISummaryItem(SummaryItem):
    order = 300
    template = 'uwsgi/homepage/site_summary_uwsgi.html'

    def get_context(self):
        return {'workers': uwsgi.numproc}

@hooks.register('construct_homepage_summary_items')
def add_uwsgi_summary_item(request, items):
    items.append(uWSGISummaryItem(request))


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^uwsgi/', include(urls)),
    ]

class uWSGIMenuItem(MenuItem):
    def is_shown(self, request):
        return request.user.is_staff


@hooks.register('register_settings_menu_item')
def register_uwsgi_menu_item():
    return uWSGIMenuItem(_('uWSGI Status'), reverse_lazy('uwsgi_index'), classnames='icon icon-cog', order=800)
