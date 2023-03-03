from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('proceso',views.proceso,name='proceso'),
    path('bienvenida',views.bienvenida,name='bienvenida'),
    path('multiplicacion',views.multiplicacion,name='multiplicacion'),
    path('division',views.division,name='division'),
    path('resta',views.resta,name='resta'),
    path('suma',views.suma,name='suma'),
    
]
        