from django.db import models

class User(models.Model):
    nome = models.TextField(max_length=50)
    descricao = models.TextField()
    data_hora = models.DateField()
    local = models.TextField(blank=True, null=True)
    Categoria = models.TimeField(blank=True, null=True)

