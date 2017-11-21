from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver

from samba.accounts.models import Dono
from samba.geo.models import Municipio


class Plano(models.Model):
    """
    Representa um plano de saneamento.
    """

    class Meta:
        verbose_name = _('plano')
        verbose_name_plural = _('planos')

    # O dono do plano, por enquanto usa User do django auth
    dono = models.ForeignKey(Dono, verbose_name=_('dono'), related_name='planos', null=True)

    # O município do plano
    municipio = models.ForeignKey(
        Municipio, models.CASCADE, verbose_name=_('município')
    )

    # O ano do plano
    ano = models.IntegerField(_('ano'), default=timezone.now().year)

    def __str__(self):
        return '{} - {} ({})'.format(
            self.municipio.nome, self.municipio.UF.sigla, self.ano
        )


class Indicador(models.Model):
    """
    Representa o valor de um indicador de um plano.
    """

    class Meta:
        verbose_name = _('valor do indicador')
        verbose_name_plural = _('valores dos indicadores')

    # O plano que esse indicador pertence.
    plano = models.ForeignKey(Plano, verbose_name=_('plano'))

    # Sigla do indicador
    sigla = models.CharField(_('sigla'), max_length=20)

    # O valor do indicador
    valor = models.CharField(_('valor'), max_length=200)

    # A descrição do valor do indicador, se for exigida
    descricao = models.TextField(
        _('descrição do valor do indicador'), blank=True
    )

    def __str__(self):
        return '{}: {} {}'.format(self.sigla, self.valor, self.descricao)


class Aquisicao(models.Model):
    """
    Representa uma aquisição de plugin.
    """

    class Meta:
        verbose_name = _('aquisição')
        verbose_name_plural = _('aquisições')

    # O plano que adquiriu o plugin
    plano = models.ForeignKey(Plano, verbose_name=_('plano'))

    # O nome do plugin que foi adquirido.
    plugin = models.CharField(_('nome'), max_length=100)

    def __str__(self):
        return self.plugin


class Gestor(models.Model):

    class Meta:
        verbose_name = _('Gestor')
        verbose_name_plural = _('Gestores')

    # sub-donos do projeto. Podem editar os campos.
    plano = models.ForeignKey(Plano,  verbose_name=_('gestores'), related_name='gestores_set', on_delete=models.CASCADE)

    # usuario associado ao gestor
    user = models.OneToOneField(User, verbose_name=_("Usuário no sistema"), related_name='gestor',
                                on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name


@receiver(post_delete, sender=Gestor)
def delete_related_user(sender, instance, **kwargs):
    instance.user.delete()
