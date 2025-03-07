from django.urls import path
from .import views

urlpatterns = [
    path("",views.lista_postagem, name='lista_postagem'),
]