from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class Dono(models.Model):

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural= _('Clientes')

    TIPO_PLANO = ((_('basico'), _('Básico')), ('premium', 'Premium'), ('enterprise', 'Enterprise'))

    # usuario associado ao perfil
    user = models.OneToOneField(User, models.CASCADE, verbose_name=_("Usuário do sistema"), related_name='dono')

    # tipo do plano do usuario
    tipo_conta = models.CharField(_("Tipo de conta"), choices=TIPO_PLANO, max_length=255)

    def __str__(self):
        return '{} - {}'.format(
            self.user.first_name, self.tipo_conta
        )
