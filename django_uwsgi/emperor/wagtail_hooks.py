from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)
from .models import Vassal
from .admin import VassalFields


class VassalModelAdmin(VassalFields, ModelAdmin):
    model = Vassal
    menu_icon = 'cogs'
    menu_order = 800
    add_to_settings_menu = True

modeladmin_register(VassalModelAdmin)
