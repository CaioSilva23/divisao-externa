from django.urls import path
from . import views


urlpatterns = [
    #OM
    path('home_oms/', views.home_oms, name='home_oms'),
    path('deletar_om/<str:id>', views.deletar_om, name='deletar_om'),
    path('dados_om/<str:id>/', views.dados_om_id, name='dados_om_id'),
    path('om_empenhos/', views.om_empenhos, name='om_empenhos'),
    path('om_empenhos_id/<str:id>/', views.om_empenhos_id, name='om_empenhos_id'),

    
]
