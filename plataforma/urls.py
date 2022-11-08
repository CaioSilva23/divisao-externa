from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('dados_om/<str:id>/', views.dados_om_id, name='dados_om_id'),
    path('om_empenhos/', views.om_empenhos, name='om_empenhos'),
    path('om_empenhos_id/<str:id>/', views.om_empenhos_id, name='om_empenhos_id'),
    path('inserir_empenho/<str:id>/', views.inserir_empenho, name='inserir_empenho'),
    path('listar_empenhos/', views.listar_empenhos, name='listar_empenhos'),
    path('remover_empenho/<str:id>/', views.remover_empenho, name="remover_empenho"),
]
