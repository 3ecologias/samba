from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext, ugettext_lazy as _

from .models import Plano, Aquisicao


class PlanoForm(ModelForm):
    class Meta:
        model = Plano
        fields = ['municipio', 'ano']


class AquisicaoForm(ModelForm):
    class Meta:
        model = Aquisicao
        fields = ['plano']

class GestorForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username","email","first_name", "last_name")
        help_texts = {
            'username': _("O nome de usuário será composto pelo nome do usuário digitado abaixo + nome do município. Ex: mariaRecife, joãoPaudalho, etc..")
        }

class GestorEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ("username", "email", "first_name", "last_name", "password")
        help_texts = {
            'username': _("O nome de usuário será composto pelo nome do usuário digitado abaixo + nome do município. Ex: mariaRecife, joãoPaudalho, etc..")
        }
