from django.urls import path
from . import views


urlpatterns = [
     #EMPENHOS
    path('inserir_empenho/<str:id>/', views.inserir_empenho, name='inserir_empenho'),
    path('listar_empenhos/', views.listar_empenhos, name='listar_empenhos'),
    path('remover_empenho/<str:id>/', views.remover_empenho, name="remover_empenho"),
    path('entregue/<int:id>/', views.entregue, name='entregue' ),
]
