#aqui toda a lógica para poder cadastrar listar atualizar e deletar boookssss
from django.shortcuts import render
from .models import Livro
from .serializers import LivroSerializers
from rest_framework import viewsets #django usa esse viewsets para gerar automaticamente a interface junto com router
# Create your views here.
#hum
class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all() #buscando
    serializer_class = LivroSerializers #usa o serializer criado







