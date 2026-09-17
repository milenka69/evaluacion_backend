from django.contrib import admin
from django.urls import path
from Tienda import views

urlpatterns = [
    path('', views.home, name='home'),
    path('juego/<int:id>/', views.juego, name='juego')
]
