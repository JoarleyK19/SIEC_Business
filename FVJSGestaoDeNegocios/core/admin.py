from django.contrib import admin

from.models import Servico, ServicoAdicionais


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('service', 'imagem', 'ativo', 'modificado')


@admin.register(ServicoAdicionais)
class ServicoAdicionalAdmin(admin.ModelAdmin):
    list_display = ('serviceAd', 'imagemAd', 'ativo', 'modificado')
