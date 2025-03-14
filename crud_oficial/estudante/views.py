from django.shortcuts import render
from .models import Aluno
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#Get all aluno
@api_view(['GET'])
def list_all(req):
    all_alunos = Aluno.objects.all()
    serializer = AlunoSerializer(all_alunos, many=True)
    return Response(serializer.data)

# Get aluno object by ID
@api_view(['GET'])
def aluno_by_id(request, pk):
    try:
        aluno_by_pk = Aluno.objects.get(pk=pk)
    except Aluno.DoesNotExist:
        return Response(
            f"Error: {status.HTTP_404_NOT_FOUND} NOT FOUND", 
            status=status.HTTP_404_NOT_FOUND
            )

    serializer = AlunoSerializer(aluno_by_pk)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_aluno(req):
    if req.method == 'POST':
        serializer = AlunoSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_aluno(req, pk):
    try:
        aluno_to_update = Aluno.objects.get(pk=pk)
    except Aluno.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AlunoSerializer(aluno_to_update, data=req.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_aluno(req,pk):
    try:
        aluno_to_delete = Aluno.objects.get(pk=pk)
    except Aluno.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    aluno_to_delete.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def print_text(req, text):
    import pyfiglet
    field = pyfiglet.figlet_format(text)

    return Response(field, status=status.HTTP_200_OK)