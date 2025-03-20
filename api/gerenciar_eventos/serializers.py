from .models import Evento
from ModelSerializer import rest_framework

class EventoSerializer(serializers.Modelserializer):
    class Meta:
        model = Evento
        fields = '__all__'
