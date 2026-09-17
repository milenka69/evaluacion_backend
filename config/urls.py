from django.contrib import admin
from django.urls import path
from Tienda import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('juego/<int:id>/', views.juego, name='detalle')
]
