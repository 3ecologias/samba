from django.conf.urls import url

from samba.plan import views

urlpatterns = [
    url(r'^planos$', views.plan_list, name='plan_list'),
    url(r'^planos/novo$', views.plan_create, name='plan_create'),
    url(r'^planos/(?P<pk>[0-9]+)$', views.plan_view, name='plan_view'),
    url(r'^planos/(?P<pk>[0-9]+)/editar$', views.plan_edit, name='plan_edit'),
    url(r'^planos/(?P<pk>[0-9]+)/apagar$', views.plan_delete, name='plan_delete'),
    url(r'^planos/(?P<pk>[0-9]+)/relatorio$', views.plan_report, name='plan_report'),
    url(r'^loja$', views.plugin_list, name='plugin_list'),
    url(r'^loja/(?P<slug>[a-z\-]+)$', views.plugin_buy, name='plugin_buy')
]
