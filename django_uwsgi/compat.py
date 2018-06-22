import django
import wagtail


if django.VERSION >= (2, 0):
    from django.urls import reverse_lazy, include, re_path as url
elif django.VERSION < (2, 0):
    from django.core.urlresolvers import reverse_lazy
    from django.conf.urls import include, url


if wagtail.VERSION >= (2, 0):
    from wagtail.admin.menu import MenuItem
    from wagtail.admin.site_summary import SummaryItem
    from wagtail.core import hooks
elif wagtail.VERSION < (2, 0):
    from wagtail.wagtailadmin.menu import MenuItem
    from wagtail.wagtailadmin.site_summary import SummaryItem
    from wagtail.wagtailcore import hooks
