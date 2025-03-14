from django.db import models

CURSOS = [
    ('DS', 'Desenvolvimento de Sistemas'),
    ('MEC', 'Mecânica')
]

INSTITUICOES = [
    ('Roberto Mange', 'Roberto Mange'),
    ('Maria Matosinho', 'Maria Matosinho')
]

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.PositiveIntegerField()
    curso = models.CharField(max_length=50, choices=CURSOS)  
    instituicao = models.CharField(max_length=100, choices=INSTITUICOES)  
    rm = models.PositiveIntegerField()  

    def __str__(self):
        return f'{self.rm} - {self.nome}'
