#criei com CLASSED BASED VIEWS

from django.shortcuts import render
from .models import Professor, Disciplina,Reserva
from rest_framework import viewsets ,permissions##criar o crud
from .serializers import ProfessorSerializer,DisciplinaSerializer,ReservaSerializer


class IsGestorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all() #lista e busca todos os professores para a filtragem
    serializer_class = ProfessorSerializer # pega o serializer de professor
    permission_classes = [IsGestorOrReadOnly]


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsGestorOrReadOnly]

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsGestorOrReadOnly]
