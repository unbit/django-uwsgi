from debug_toolbar.panels import Panel
from django.utils.translation import ugettext_lazy as _
from . import uwsgi


class UwsgiPanel(Panel):
    '''
    uWSGI Debug Toolbar Panel
    '''
    title = _('uWSGI Status')
    nav_title = _('uWSGI Status')
    template = 'uwsgi/panel.html'

    @property
    def nav_subtitle(self):
        if uwsgi is not None:
            status = _('Version %s, %d Workers') % (
                str(uwsgi.version.decode()), int(uwsgi.numproc))
        else:
            status = _('uWSGI is missing =(')
        return status

    def process_response(self, request, response):
        if uwsgi is None:
            self.record_stats({'unavailable': True})
        else:
            from .stats import get_uwsgi_stats
            self.record_stats(get_uwsgi_stats())
