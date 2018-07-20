import wagtail


if wagtail.VERSION >= (2, 0):
    from wagtail.admin.menu import MenuItem
    from wagtail.admin.site_summary import SummaryItem
    from wagtail.core import hooks
elif wagtail.VERSION < (2, 0):
    from wagtail.wagtailadmin.menu import MenuItem
    from wagtail.wagtailadmin.site_summary import SummaryItem
    from wagtail.wagtailcore import hooks
