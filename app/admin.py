from django.contrib import admin

from .models import *

class ItemAdmin(admin.ModelAdmin):
    search_fields = ('detalle','codigo_barras',)

admin.site.register([
    Articulo
], ItemAdmin)
