from django.http import Http404
from django.utils.text import slugify

from samba.plan.models import Indicador as IndicadorModel


class PluginError(Exception):
    """
    Erro levantado quando ocorre algum erro de inicialização
    ou lógica de um plugin.
    """
    pass


class PluginMeta(type):
    """
    Metaclasse de um plugin, usada para registrar plugins
    automaticamente.
    """
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'):
            cls.plugins = {}
        else:
            if not hasattr(cls, 'nome'):
                raise PluginError('Um plugin deve possuir um nome')

            if not hasattr(cls, 'slug'):
                cls.slug = slugify(cls.nome)

            if not hasattr(cls, 'descricao'):
                raise PluginError('Um plugin deve possuir uma descrição')

            cls.plugins[cls.slug] = cls


class Plugin(object, metaclass=PluginMeta):
    """
    Classe base de um plugin.

    Um plugin possui os dados relativos a ele como nome, descrição
    e preço.
    """
    def __str__(self):
        return self.nome


class _Indicador(object):
    """
    Representa um indicador associado a um plano.
    """
    def __init__(self, plano, sigla, nome, unidade=None, definicao=None,
                 model=None, exige_descricao=False, escolhas=None,
                 multipla_escolha=False, subcategoria=None, calcular=None,
                 paragrafo=False, fonte=None):
        if model is None:
            model = IndicadorModel(plano=plano, sigla=sigla)

        self._plano = plano
        self._model = model

        self.sigla = sigla
        self.nome = nome
        self.unidade = unidade
        self.definicao = definicao
        self.exige_descricao = exige_descricao
        self.escolhas = escolhas
        self.multipla_escolha = multipla_escolha
        self.subcategoria = subcategoria
        self.calcular = calcular
        self.paragrafo = paragrafo
        self.fonte = fonte

    @property
    def calculado(self):
        """
        Se o indicador é de valor calculado.
        """
        return callable(self.calcular)

    @property
    def valor(self):
        if self.calculado:
            def get_valor(sigla):
                try:
                    # TODO: Suporte a calcular a partir de indicadores calculados?
                    indicador = self._plano.indicador_set.get(sigla=sigla)
                    try:
                        return int(indicador.valor)
                    except ValueError:
                        return None
                except IndicadorModel.DoesNotExist:
                    return None

            return self.calcular(get_valor)

        return self._model.valor

    @property
    def valores(self):
        if self.multipla_escolha:
            return self.valor.split(', ')
        else:
            return list(self.valor)

    @valor.setter
    def valor(self, valor):
        if self.calculado:
            return

        if self.multipla_escolha:
            valor = ', '.join(valor)

        self._model.valor = valor

    @property
    def descricao(self):
        return getattr(self._model, 'descricao')

    @descricao.setter
    def descricao(self, descricao):
        self._model.descricao = descricao

    def save(self):
        if self.calculado:
            return

        self._model.save()

    def __str__(self):
        return '({}) {}'.format(self.sigla, self.nome)


class _PluginInstance(object):
    """
    Ponte entre um plugin e os dados dos indicadores de um plano.
    """
    def __init__(self, plugin, plano):
        self._plugin = plugin
        self._plano = plano

    @property
    def slug(self):
        return getattr(self._plugin, 'slug')

    @property
    def nome(self):
        return getattr(self._plugin, 'nome')

    @property
    def descricao(self):
        return getattr(self._plugin, 'descricao')

    @property
    def preco(self):
        return getattr(self._plugin, 'preco')

    @property
    def indicadores(self):
        if not hasattr(self._plugin, 'indicadores'):
            return None

        indicadores = []

        for sigla, dados in self._plugin.indicadores:
            model = None

            try:
                model = self._plano.indicador_set.get(sigla=sigla)
            except IndicadorModel.DoesNotExist:
                pass

            indicador = _Indicador(
                plano=self._plano, sigla=sigla, model=model, **dados
            )

            indicadores.append(indicador)

        return indicadores
        
    @property
    def icone_sidebar(self):
        return getattr(self._plugin, 'icone_sidebar')

    def __str__(self):
        return '{} ({})'.format(self.plugin.nome, self.plano.municipio)


def get_plugin_or_404(slug):
    """
    Obtêm um plugin a partir de sua slug.
    Se não existir nenhum plugin correspondente, gera um 404.
    """
    if slug not in Plugin.plugins:
        raise Http404('O plugin {} não existe'.format(slug))

    return Plugin.plugins.get(slug)


def get_all_plugins():
    """
    Obtêm uma lista com todos os plugins carregados.
    """
    return [p() for p in Plugin.plugins.values()]


def get_plano_plugins(plano):
    """
    Obtêm uma lista com os todos os plugins de um plano.
    """
    plugins = []

    for aquisicao in plano.aquisicao_set.all():
        if aquisicao.plugin in Plugin.plugins:
            plugin = Plugin.plugins.get(aquisicao.plugin)
            plugins.append(_PluginInstance(plugin, plano))

    return plugins
