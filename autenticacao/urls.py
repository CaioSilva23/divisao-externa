from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_auth, name='home_auth'),

    path('logar/', views.logar, name='logar'),
    path('sair/', views.sair, name='sair'),
]
