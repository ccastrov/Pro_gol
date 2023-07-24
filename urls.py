from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
# path('mostrar_formulario/', views.mostrar_formulario, name='mostrar_formulario'),
]
