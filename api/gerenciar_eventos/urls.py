from django.urls import path
from .views import EventoListCreateView, EventoDetailView, EventosProximosView, EventoDetalhesView

urlpatterns = [
    path ('eventos/', EventoListCreateView.as_view(), name='eventos-list'),
    path ('eventos/<int:id>/', EventoDetailView.as_view(), name='evento-detail'),
    path ('eventos/proximos/', EventosProximosView.as_view(), name='eventos-proximos'),
    path ('eventos/<int:id>/detalhes/', EventoDetalhesView.as_view(), name="eventos-detail-id")


]

