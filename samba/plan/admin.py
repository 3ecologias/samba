from django.contrib import admin

from .models import Aquisicao, Indicador, Plano, Gestor


class AquisicaoInline(admin.TabularInline):
    model = Aquisicao


class IndicadorInline(admin.StackedInline):
    model = Indicador

class GestoresInline(admin.TabularInline):
    model = Gestor


class PlanoAdmin(admin.ModelAdmin):
    inlines = [IndicadorInline, AquisicaoInline, GestoresInline]


admin.site.register(Plano, PlanoAdmin)
