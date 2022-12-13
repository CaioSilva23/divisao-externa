from django.urls import path
from . import views


urlpatterns = [

    path('home/', views.home, name='home'),


    # FORNECEDORES
    path('fornecedores/', views.fornecedores, name='fornecedores'),
    path('inserir_fornecedor/', views.inserir_fornecedor, name='inserir_fornecedor'),
    path('deletar_fornecedor/<int:id>', views.deletar_fornecedor, name='deletar_fornecedor'),


    path('credito/', views.credito, name='credito'),
    path('nc/<int:id>', views.nc, name='nc'),


    path('inserir_demanda', views.inserir_demanda, name='inserir_demenda'),

]
