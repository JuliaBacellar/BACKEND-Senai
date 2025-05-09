from django.urls import path, include
from rest_framework import routers
from .views import ProfessorViewSet, DisciplinaViewSet, ReservaViewSet

#default router facilita o roteamento de urls para viewsets,gera urls automaticas
router = routers.DefaultRouter()
router.register(r'professores', ProfessorViewSet)
router.register(r'disciplinas',DisciplinaViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]