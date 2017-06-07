from django.shortcuts import render
from django.contrib.auth import views as auth_views


def login(request):
    """
    Página de login.
    """
    return auth_views.login(request,
                            template_name='accounts/login.html')


def logout(request):
    """
    Página de logout.
    """
    return auth_views.logout(request, next_page='/')


def password_reset(request):
    """
    Página de solicitação de redefinição de senha.
    """
    return auth_views.password_reset(
      request,
      template_name='accounts/password_reset.html',
      email_template_name='accounts/password_reset_email.html',
      subject_template_name='accounts/password_reset_subject.txt'
    )


def password_reset_done(request):
    """
    Página que exibe a mensagem que o e-mail de redefinição de senha
    foi enviado.
    """
    return auth_views.password_reset_done(
        request,
        template_name='accounts/password_reset_done.html'
    )


def password_reset_confirm(request, uidb64=None, token=None):
    """
    Página para redefinir a senha de uma conta, acessível apenas
    quando o usuário solicitou isso.
    """
    return auth_views.password_reset_confirm(
        request,
        uidb64=uidb64, 
        token=token,
        template_name='accounts/password_reset_confirm.html'
    )


def password_reset_complete(request):
    """
    Página que senha conta foi redefinida com sucesso.
    """
    return auth_views.password_reset_complete(
        request,
        template_name='accounts/password_reset_complete.html'
    )
