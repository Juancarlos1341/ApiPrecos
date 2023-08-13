from django.contrib import admin
from Precos.models import Precos

class Admin_Precos(admin.ModelAdmin):
    list_display = ('Produto',)
    list_display_links = ('Produto',)
    search_fields = ('Codigo','Produto')

admin.site.register(Precos,Admin_Precos)

