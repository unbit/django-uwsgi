from debug_toolbar.panels import Panel
try:
    from django.utils.translation import ugettext_lazy as _
except ImportError:
    from django.utils.translation import ngettext_lazy as _
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

    def generate_stats(self, request, response):
        if uwsgi is None:
            self.record_stats({'unavailable': True})
        else:
            from .stats import get_uwsgi_stats
            self.record_stats(get_uwsgi_stats())
    process_response = generate_stats
