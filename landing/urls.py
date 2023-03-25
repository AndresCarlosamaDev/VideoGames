from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('perfil/<str:usuario>', views.perfil, name='perfil'),
    path('cerrarSesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('reingresar/', views.reingresar_Sesion, name='reingresar_sesion'),
    path('addJuego/', views.addJuego, name='addJuego'),
    path('completar/<int:id>/', views.completar, name='completar'),
    
]
