from django.contrib import admin
from caixas.models import *

class Admin_Caixas(admin.ModelAdmin):
    list_display = ('DataInicial','SaldoInicial','TotalCaixa')
    list_display_links = ('DataInicial',)
    search_fields = ('DataInicial','Operador')

class Admin_Entrada_de_Notas(admin.ModelAdmin):
    list_display = ('Fornecedor','TotalPagar','TipoDeEntrada')
    list_display_links = ('Fornecedor',)
    search_fields = ('Fornecedor',)

class Admin_Sangria(admin.ModelAdmin):
    list_display = ('Descriacao','Total',)
    list_display_links = ('Descriacao',)
    search_fields = ('Descriacao','Total')


admin.site.register(CaixasHf, Admin_Caixas)
admin.site.register(CaixasSm, Admin_Caixas)
admin.site.register(Entrada_de_notas_Hf, Admin_Entrada_de_Notas)
admin.site.register(Entrada_de_notas_Sm, Admin_Entrada_de_Notas)
admin.site.register(Sangria_Hf, Admin_Sangria)
admin.site.register(Sangria_Sm, Admin_Sangria)