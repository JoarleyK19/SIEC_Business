from django.contrib import admin

from.models import Servico, ServicoAdicionais, Cargo, Funcionario, EmpresasParceiras


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('service', 'imagem', 'ativo', 'modificado')


@admin.register(ServicoAdicionais)
class ServicoAdicionalAdmin(admin.ModelAdmin):
    list_display = ('serviceAd', 'imagemAd', 'ativo', 'modificado')


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')


@admin.register(EmpresasParceiras)
class EmpresaParceiraAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'ativo', 'modificado')
