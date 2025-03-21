from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from .models import Evento
from .serializers import EventoSerializer

class EventoListCreateView(APIView):
    def get(self, request):
        eventos = Evento.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventoDetailView(APIView):
    def get_object(self, id):
        try:
            return Evento.objects.get(id=id)
        except Evento.DoesNotExist:
            return None

    def get(self, request, id):
        evento = self.get_object(id)
        if evento is None:
            return Response({"erro": "Evento não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventoSerializer(evento)
        return Response(serializer.data)

    def put(self, request, id):
        evento = self.get_object(id)
        if evento is None:
            return Response({"erro": "Evento não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventoSerializer(evento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        evento = self.get_object(id)
        if evento is None:
            return Response({"erro": "Evento não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        evento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EventosProximosView(APIView):

    def get(self, request):
        data_atual = now()
        data_limite = data_atual + timedelta(days=7) 
        eventos = Evento.objects.filter(data_hora__gte=data_atual, data_hora__lte=data_limite)
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)

class EventoDetalhesView(APIView):
   
    def get(self, request, id):
        try:
            evento = Evento.objects.get(id=id)
        except Evento.DoesNotExist:
            return Response({"erro": "Evento não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        detalhes = {
            "nome": evento.nome,
            "descricao": evento.descricao,
            "data": evento.data_hora,
            "local": evento.local,
            "categoria": evento.categoria,
        }
        return Response(detalhes, status=status.HTTP_200_OK)
    
