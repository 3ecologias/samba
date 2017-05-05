from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext, ugettext_lazy as _
from . import autocomplete

from .models import Plano, Aquisicao


class PlanoForm(ModelForm):
    class Meta:
        model = Plano
        fields = ['municipio', 'ano']
        widgets = {
            'municipio': autocomplete.ModelSelect2Pt(
            url='municipio_autocomplete',
            )
        }


class AquisicaoForm(ModelForm):
    class Meta:
        model = Aquisicao
        fields = ['plano']

class GestorForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username","email","first_name", "last_name")
        help_texts = {
            'username': _("Crie um usuário com nomeSobrenome. ex: mariaSilva")
        }

class GestorEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ("username", "email", "first_name", "last_name", "password")
        help_texts = {
            'username': _("Crie um usuário com nomeSobrenome. ex: mariaSilva")
        }
