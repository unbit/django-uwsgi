from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Vassal


def enabled(modeladmin, request, queryset):
    queryset.update(enabled='1')
enabled.short_description = _("Enable selected Emperor's Vassals")


def disabled(modeladmin, request, queryset):
    queryset.update(enabled='0')
disabled.short_description = _("Disable selected Emperor's Vassals")


class VassalFields(object):
    list_display = ('title', 'extension', 'updated', 'created', 'enabled', 'ts')
    search_fields = ['title']
    list_filter = ('enabled', 'created', 'extension')


class VassalAdmin(VassalFields, admin.ModelAdmin):
    actions = [enabled, disabled]

admin.site.register(Vassal, VassalAdmin)
