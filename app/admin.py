from django.contrib import admin

from .models import *

class ItemAdmin(admin.ModelAdmin):
    search_fields = ('descripcion','codigo_barras',)

admin.site.register([
    Articulo
], ItemAdmin)
