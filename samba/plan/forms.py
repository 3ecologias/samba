from django.forms import ModelForm

from .models import Plano, Aquisicao


class PlanoForm(ModelForm):
    class Meta:
        model = Plano
        fields = ['municipio', 'ano']


class AquisicaoForm(ModelForm):
    class Meta:
        model = Aquisicao
        fields = ['plano']
