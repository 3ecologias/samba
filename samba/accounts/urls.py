from django.conf.urls import url

from samba.accounts import views

urlpatterns = [
    url(r'^entrar$', views.login, name='login'),
    url(r'^sair$', views.logout, name='logout'),
    url(r'^redefinir-senha$', views.password_reset, name='password_reset'),
    url(r'^redefinir-senha/pronto$',
        views.password_reset_done, name='password_reset_done'),
    url(r'^redefinir/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^redefinir/pronto$', views.password_reset_complete,
        name='password_reset_complete'),
]
