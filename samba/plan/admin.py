from django.contrib import admin

from .models import Aquisicao, Indicador, Plano


class AquisicaoInline(admin.TabularInline):
    model = Aquisicao


class IndicadorInline(admin.StackedInline):
    model = Indicador


class PlanoAdmin(admin.ModelAdmin):
    inlines = [IndicadorInline, AquisicaoInline]


admin.site.register(Plano, PlanoAdmin)
