from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Plano, Indicador
from .plugins import get_plugin_or_404, get_all_plugins, get_plano_plugins
from .forms import PlanoForm, AquisicaoForm


@login_required
def plan_list(request):
    return render(request, 'plan/plan_list.html', {
      'user': request.user,
      'planos': Plano.objects.filter(dono=request.user.dono)
    })


@login_required
def plan_create(request):
    if request.method == 'POST':
        form = PlanoForm(request.POST)

        if form.is_valid():
            plano = form.save(commit=False)
            plano.dono = request.user.dono
            plano.save()
            return redirect('plan_view', pk=plano.id)
    else:
        form = PlanoForm()

    return render(request, 'plan/plan_create.html', {
        'user': request.user,
        'form': form
    })


def plan_view(request, pk):
    plano = get_object_or_404(Plano, pk=pk)
    plugins = get_plano_plugins(plano)

    return render(request, 'plan/plan_view.html', {
        'user': request.user,
        'plano': plano,
        'gestores': plano.gestores_set.all(),
        'plugins': plugins
    })


@login_required
def plan_edit(request, pk):
    plano = get_object_or_404(Plano, pk=pk)
    plugins = get_plano_plugins(plano)

    if plano.dono.user != request.user and not plano.gestores_set.filter(user_id=request.user.id).exists():
        # TODO: Informar que o usuário não possui
        # permisão suficiente para editar o plano
        return redirect('/')

    if request.method == 'POST':
        for plugin in plugins:
            if not hasattr(plugin, 'indicadores'):
                continue

            for indicador in plugin.indicadores:
                if indicador.sigla not in request.POST or indicador.calculado:
                    continue

                if indicador.multipla_escolha:
                    # Indicadores de múltipla escolha tem os valores
                    # salvos como uma lista separada por vírgula
                    indicador.valor = request.POST.getlist(indicador.sigla)
                else:
                    indicador.valor = request.POST.get(indicador.sigla)

                if indicador.exige_descricao:
                    # A descrição de cada indicador é passada no formulário
                    # na forma {sigla}_descricao
                    indicador.descricao = request.POST.get(indicador.sigla + '_descricao')

                indicador.save()

        return redirect('plan_view', pk=pk)

    return render(request, 'plan/plan_edit.html', {
        'user': request.user,
        'plano': plano,
        'plugins': plugins
    })


@login_required
def plan_delete(request, pk):
    pass


def plan_report(request, pk):
    plano = get_object_or_404(Plano, pk=pk)
    plugins = get_plano_plugins(plano)
    indicadores = {}
    descricao = {}

    # Transforma a lista de indicadores de todos os plugins
    # em um dicionário com os valores dos indicadores por sigla
    for plugin in plugins:
        if not hasattr(plugin, 'indicadores'):
            continue

        for indicador in plugin.indicadores:
            indicadores[indicador.sigla] = indicador.valor
            descricao[indicador.sigla] = indicador.descricao

    return render(request, 'plan/plan_report.html', {
        'user': request.user,
        'plano': plano,
        'indicadores': indicadores,
        'descricao': descricao
    })


@login_required
def plugin_list(request):
    plugins = get_all_plugins()

    return render(request, 'plan/plugin_list.html', {
        'user': request.user,
        'plugins': plugins
    })


@login_required
def plugin_buy(request, slug):
    plugin = get_plugin_or_404(slug)
    queryset = Plano.objects.filter(dono=request.user.dono) \
                            .exclude(aquisicao__plugin=slug)

    if request.method == 'POST':
        form = AquisicaoForm(request.POST)

        if form.is_valid():
            aquisicao = form.save(commit=False)
            aquisicao.plugin = plugin.slug
            aquisicao.save()
            return redirect('plan_view', pk=aquisicao.plano.pk)
    else:
        form = AquisicaoForm()
        form.fields['plano'].queryset = queryset

    return render(request, 'plan/plugin_buy.html', {
        'user': request.user,
        'form': form,
        'plugin': plugin
    })
