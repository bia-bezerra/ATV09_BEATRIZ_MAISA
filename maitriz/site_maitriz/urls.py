from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('conteudo/<slug:slug>/', views.conteudo, name='conteudo'),
]