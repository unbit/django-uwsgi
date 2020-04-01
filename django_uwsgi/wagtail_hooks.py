from django.utils.translation import ugettext_lazy as _

from . import uwsgi, urls
from .compat import include, url, reverse_lazy
from .wagtail_compat import hooks, MenuItem, SummaryItem


class UwsgiSummaryItem(SummaryItem):
    order = 800
    template = 'uwsgi/wagtail_dashboard_item.html'

    def get_context(self):
        workers = int(uwsgi.numproc) if uwsgi else 0
        return {'workers': workers}


@hooks.register('construct_homepage_summary_items')
def add_uwsgi_summary_item(request, items):
    items.append(UwsgiSummaryItem(request))


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^uwsgi/', include(urls)),
    ]


class UwsgiMenuItem(MenuItem):
    def is_shown(self, request):
        return request.user.is_staff


@hooks.register('register_settings_menu_item')
def register_uwsgi_menu_item():
    return UwsgiMenuItem(_('uWSGI Status'), reverse_lazy('uwsgi_index'), classnames='icon icon-cogs', order=800)
