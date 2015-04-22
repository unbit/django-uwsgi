from django.contrib import admin
from .models import Vassal


class VassalAdmin(admin.ModelAdmin):
    list_display = ['title', 'extension', 'updated', 'created', 'enabled', 'ts']
    search_fields = ['title']
    list_filter = ('enabled', 'created', 'extension')

admin.site.register(Vassal, VassalAdmin)
