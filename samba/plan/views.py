from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Plano, Indicador, Gestor
from samba.accounts.models import Dono
from .plugins import get_plugin_or_404, get_all_plugins, get_plano_plugins
from .forms import PlanoForm, AquisicaoForm, GestorForm, GestorEditForm
from django.http import HttpResponseForbidden


@login_required
def plan_list(request):
    return render(request, 'plan/plan_list.html', {
      'user': request.user,
      'planos': Plano.objects.filter(dono=request.user.dono)
    })

@login_required
def plan_upgrade(request):
    dono = get_object_or_404(Dono, user=request.user)
    return render(request, 'plan/plan_upgrade.html', {
      'user': request.user,
      'tipo': dono.tipo_conta
    })

#funcao auxiliar para checar se pode ou nao criar novos planos baseado no tipo de conta
def plan_create_check(dono):
    num_planos = dono.planos.count()
    if dono.tipo_conta == 'basico' and num_planos == 0:
        return True
    elif dono.tipo_conta == 'premium' and num_planos < 5:
        return True
    elif dono.tipo_conta == 'enterprise' and num_planos < 10:
        return True
    else:
        return False

@login_required
def plan_create(request):
    dono = Dono.objects.get(user=request.user)
    checked = plan_create_check(dono)
    if checked:
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
    else:
        return redirect('plan_upgrade')


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
        # Não permitido pois nao tem permissao nem de gestor nem de dono do plano
        return HttpResponseForbidden()

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

@login_required
def gestor_list(request, pk):
    plano = get_object_or_404(Plano, pk=pk)

    return render(request, 'plan/gestor_list.html', {
        'plano': plano,
        'gestores': plano.gestores_set.all(),
    })

@login_required
def gestor_create(request, pk):
    plano = get_object_or_404(Plano, pk=pk)

    if request.method == 'POST':
        form = GestorForm(request.POST)

        if form.is_valid():
            gestor_user = form.save(commit=False)
            gestor_user.username = gestor_user.username+plano.municipio.nome
            gestor_user.save()
            gestor= Gestor.objects.create(
                user=gestor_user,
                plano=plano
            )
            return redirect('gestor_list', pk=plano.id)
    else:
        form = GestorForm()

    return render(request, 'plan/gestor_create.html', {
        'plano': plano,
        'form': form,
    })

@login_required
def gestor_edit(request, pk, gestor_pk):
    plano = get_object_or_404(Plano, pk=pk)
    gestor = get_object_or_404(Gestor, pk=gestor_pk)

    if plano.dono.user != request.user:
        # Não permitido, nao e o dono do projeto
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = GestorEditForm(data=request.POST, instance=gestor.user)

        if form.is_valid():
            gestor_user = form.save()
            gestor.user = gestor_user
            gestor.save()
            return redirect('gestor_list', pk=plano.id)
    else:
        form = GestorEditForm(instance=gestor.user)


    return render(request, 'plan/gestor_edit.html', {
        'user': request.user,
        'plano': plano,
        'gestor': gestor,
        'form': form,
    })

@login_required
def gestor_edit(request, pk, gestor_pk):
    plano = get_object_or_404(Plano, pk=pk)
    gestor = get_object_or_404(Gestor, pk=gestor_pk)

    if plano.dono.user != request.user:
        # Não permitido, nao e o dono do projeto
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = GestorEditForm(data=request.POST, instance=gestor.user)

        if form.is_valid():
            gestor_user = form.save()
            gestor.user = gestor_user
            gestor.save()
            return redirect('gestor_list', pk=plano.id)
    else:
        form = GestorEditForm(instance=gestor.user)


    return render(request, 'plan/gestor_edit.html', {
        'user': request.user,
        'plano': plano,
        'gestor': gestor,
        'form': form,
    })

@login_required
def gestor_delete(request, pk, gestor_pk):
    plano = get_object_or_404(Plano, pk=pk)
    gestor = get_object_or_404(Gestor, pk=gestor_pk)
    user = get_object_or_404(User, pk=gestor.user.id)

    if plano.dono.user != request.user:
        # Não permitido, nao e o dono do projeto
        return HttpResponseForbidden()

    if request.method == 'POST':
        if 'sim' in request.POST:
            gestor.delete()
            user.delete()
            return redirect('gestor_list', pk=plano.id)
        else:
            return redirect('gestor_list', pk=plano.id)

    return render(request, 'plan/gestor_delete_confirm.html', {
        'plano': plano,
        'gestor': gestor,
    })
