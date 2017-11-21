from django import template
from samba.plan.models import Gestor, Plano

register = template.Library()


@register.assignment_tag
def get_plan_pk_by_gestor(user):

    gestor = Gestor.objects.get(user=user)
    if gestor:
        plano = Plano.objects.get(pk=gestor.plano.pk)
        if plano:
            return plano

    return False


@register.assignment_tag
def is_plan_owner(user, pk):

    plano = Plano.objects.get(pk=pk)
    is_owner = True if plano.dono.user==user else False

    return is_owner


@register.assignment_tag
def is_plan_gestor(user, pk):

    plano = Plano.objects.get(pk=pk)
    is_gestor = True if plano.gestores_set.filter(user_id=user.id).exists() else False

    return is_gestor
