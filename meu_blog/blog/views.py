from django.shortcuts import render
from .models import Postagem
# Create your views here.

##cuidado aqui porque em um lugar esta postagens e no outro esta postagem 

def lista_postagem(request):
    postagens = Postagem.objects.all().order_by('-data_criacao')
    return render(request,'blog/lista_postagens.html', {'postagens': postagens})


