from django.urls import path
from . import views

urlpatterns = [
       #PREGÕES
    path('pregoes/', views.pregoes, name='pregoes'),
    path('inserir_pregao/', views.inserir_pregao, name='inserir_pregao'),
    path('deletar_pregao/<int:id>', views.deletar_pregao, name='deletar_pregao'),
    path('capacidade_empenho<int:id>', views.capacidade_empenho, name='capacidade_empenho'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('homologado/', views.homologado, name='homologado'),
    path('empenhado/', views.empenhado, name='empenhado'),
    path('capacidade/', views.capacidade, name='capacidade'),
    path('home_tabela/', views.home_tabela, name='home_tabela'),
]
