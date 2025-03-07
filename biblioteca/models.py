from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano_pub = models.DateField(blank=True, null=True) 
    editora = models.CharField(max_length=100, blank=True, null=True)
    idioma = models.CharField(max_length=50, default="portugues")
    descricao = models.TextField(blank=True, null=True)
    disponivel=models.BooleanField(default=True)

