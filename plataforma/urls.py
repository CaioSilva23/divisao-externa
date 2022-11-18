from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_auth, name='home_auth'),
    path('home/', views.home, name='home'),

    #OM
    path('deletar_om/<str:id>', views.deletar_om, name='deletar_om'),
    path('dados_om/<str:id>/', views.dados_om_id, name='dados_om_id'),
    path('om_empenhos/', views.om_empenhos, name='om_empenhos'),
    path('om_empenhos_id/<str:id>/', views.om_empenhos_id, name='om_empenhos_id'),

    #EMPENHOS
    path('inserir_empenho/<str:id>/', views.inserir_empenho, name='inserir_empenho'),
    path('listar_empenhos/', views.listar_empenhos, name='listar_empenhos'),
    path('remover_empenho/<str:id>/', views.remover_empenho, name="remover_empenho"),

    #PREGÕES
    path('pregoes/', views.pregoes, name='pregoes'),
    path('inserir_pregao/', views.inserir_pregao, name='inserir_pregao'),
    path('deletar_pregao/<int:id>', views.deletar_pregao, name='deletar_pregao'),

    # FORNECEDORES
    path('fornecedores/', views.fornecedores, name='fornecedores'),
    path('inserir_fornecedor/', views.inserir_fornecedor, name='inserir_fornecedor'),
    path('deletar_fornecedor/<int:id>', views.deletar_fornecedor, name='deletar_fornecedor'),


    path('credito/', views.credito, name='credito'),

]
