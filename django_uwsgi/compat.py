import django


if django.VERSION >= (2, 0):
    from django.urls import reverse_lazy, include, re_path as url
elif django.VERSION < (2, 0):
    from django.core.urlresolvers import reverse_lazy
    from django.conf.urls import include, url
