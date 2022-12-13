from django.urls import path
from . import views


urlpatterns = [

    path('home/', views.home, name='home'),


    # #PREGÕES
    # path('pregoes/', views.pregoes, name='pregoes'),
    # path('inserir_pregao/', views.inserir_pregao, name='inserir_pregao'),
    # path('deletar_pregao/<int:id>', views.deletar_pregao, name='deletar_pregao'),
    # path('capacidade_empenho<int:id>', views.capacidade_empenho, name='capacidade_empenho'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('homologado/', views.homologado, name='homologado'),
    # path('empenhado/', views.empenhado, name='empenhado'),
    # path('capacidade/', views.capacidade, name='capacidade'),
    # path('home_tabela/', views.home_tabela, name='home_tabela'),

    # FORNECEDORES
    path('fornecedores/', views.fornecedores, name='fornecedores'),
    path('inserir_fornecedor/', views.inserir_fornecedor, name='inserir_fornecedor'),
    path('deletar_fornecedor/<int:id>', views.deletar_fornecedor, name='deletar_fornecedor'),


    path('credito/', views.credito, name='credito'),
    path('nc/<int:id>', views.nc, name='nc'),


    path('inserir_demanda', views.inserir_demanda, name='inserir_demenda'),

]
