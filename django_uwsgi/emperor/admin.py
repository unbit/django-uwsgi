from django.contrib import admin
from .models import Vassal


class VassalFields(object):
    list_display = ('title', 'extension', 'updated', 'created', 'enabled', 'ts')
    search_fields = ['title']
    list_filter = ('enabled', 'created', 'extension')


class VassalAdmin(VassalFields, admin.ModelAdmin):
    pass

admin.site.register(Vassal, VassalAdmin)
