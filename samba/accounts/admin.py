from django.contrib import admin
from .models import Dono
from samba.plan.models import Plano

class PlanoInline(admin.TabularInline):
    model = Plano


class DonoAdmin(admin.ModelAdmin):
    inlines = [PlanoInline,]

admin.site.register(Dono, DonoAdmin)
