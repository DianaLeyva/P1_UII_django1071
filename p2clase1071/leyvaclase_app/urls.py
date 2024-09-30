from django.urls import path
from . import views
urlpatterns = [
    path('', views.hola, name='leyvaclase_app'),
]
