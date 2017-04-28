from django import template
from samba.plan.models import Gestor, Plano

register = template.Library()
@register.assignment_tag

def get_plan_pk_by_gestor(user):

    gestor = Gestor.objects.get(user=user)
    plano = Plano.objects.get(pk=gestor.plano.pk)
    return plano.pk
