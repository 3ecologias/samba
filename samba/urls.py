from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views import defaults as default_views
from django.views.static import serve

from samba.accounts import urls as accounts_urls
from samba.plan import urls as plan_urls
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^tools$', views.ToolsView.as_view(), name='tools'),
    url(r'', include(accounts_urls)),
    url(r'', include(plan_urls)),
    url(r'', include("annotator.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# URLs para testarmos as páginas de 404 e compania
if settings.DEBUG:
    # STATIC URL
    urlpatterns.append(url(r'^static/(?P<path>.*)$', serve ,{'document_root': settings.STATIC_ROOT}))
    # Adicionar django admin no modo debug para cadastro de dados.
    from django.contrib import admin
    urlpatterns.append(url('^admin/', admin.site.urls))

    urlpatterns += [
        url(r'^400/$', default_views.bad_request,
            kwargs={'exception': Exception('Bad Request!')}),

        url(r'^403/$', default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')}),

        url(r'^404/$', default_views.page_not_found,
            kwargs={'exception': Exception('Page not Found')}),

        url(r'^500/$', default_views.server_error),
    ]
