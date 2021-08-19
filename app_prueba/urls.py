from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio),
    #Create Read Update Delete
    path('agregar', views.agregar), #created
    path('leer', views.leer),
    path('actualizar', views.actualizar), #actualizar
    path('eliminar', views.eliminar), 
]
