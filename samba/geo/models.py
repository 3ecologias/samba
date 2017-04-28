from django.db import models
from django.utils.translation import ugettext as _


class UF(models.Model):

    """
        UF: Unidade da federação, corresponde a um estado do país.
        """
    class Meta:
        verbose_name = _('Unidade da Federação (UF)')
        verbose_name_plural = _('Unidades da Federação (UF\'s)')

    nome = models.CharField(_('nome'), max_length=100)
    sigla = models.CharField(_('sigla'), max_length=4, blank=True)
    regiao = models.CharField(_('região'), max_length=50)
    avatar = models.CharField(_('avatar'), max_length=500, blank=True)

    def __str__(self):
        return self.nome


class Municipio(models.Model):

    """
    Representa uma cidade.
    """
    class Meta:
        verbose_name = _('município')

    nome = models.CharField(_('nome'), max_length=200)
    cod_ibge = models.IntegerField(_('código do IBGE'))
    descricao = models.TextField(_('descrição'))
    UF = models.ForeignKey(UF, verbose_name=_('Unidade da Federação'))

    # avatar = models.ImageField(upload_to="municipios")

    lat = models.FloatField(_('latitude'))
    lng = models.FloatField(_('longitude'))
    alt = models.FloatField(
        _('altitude'), help_text=_('metros acima do nível do mar'))

    # slug = AutoSlugField(populate_from=nome,unique_with=['nome',],editable=True)

    # @permalink
    # def get_absolute_url(self):
    #     return ({'slug': self.slug})

    def __str__(self):
        return '{} - {}'.format(self.nome, self.UF.sigla)
