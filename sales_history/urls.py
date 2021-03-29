from django.urls import path

from . import views

urlpatterns = [

    path('', views.indicadores, name='indicadores'),
    path('tablas/', views.tablas, name='tablas'),
    path('lineatiempo/', views.visualizador, name='visualizador'),
]
