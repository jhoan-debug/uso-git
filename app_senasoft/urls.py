from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('registro/', views.registro, name='registro'),
    path('competidores/', views.competidores, name='competidores'),
]