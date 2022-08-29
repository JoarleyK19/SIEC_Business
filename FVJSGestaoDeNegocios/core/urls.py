from django.urls import path

from .views import IndexView, FormsView, SobrenosView, EmpresasView, PoliticasView, ServiceView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', FormsView.as_view(), name='contato'),
    path('servico/', ServiceView.as_view(), name='service'),
    path('sobrenos/', SobrenosView.as_view(), name='sobrenos'),
    path('empresas/', EmpresasView.as_view(), name='empresas'),
    path('politicas/', PoliticasView.as_view(), name='politicas')

]
