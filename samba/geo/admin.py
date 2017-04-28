from django.contrib import admin
from . import models

# Register your models here.


class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'UF', 'cod_ibge')
    list_filter = ['UF']
    ordering = ['nome']
    search_fields = ['nome']


class UfAdmin(admin.ModelAdmin):
    list_dislay = ('nome', 'sigla', 'regiao')
    list_filter = ['regiao']
    ordering = ['nome']
    search_fields = ['nome']

admin.site.register(models.Municipio, MunicipioAdmin)
admin.site.register(models.UF, UfAdmin)
