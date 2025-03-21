from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    data_hora = models.DateTimeField()
    local = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)

