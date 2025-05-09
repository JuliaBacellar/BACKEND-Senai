from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
#models Professores,Disciplinas e Reservas de ambientes
class Professor(models.Model):
    ni = models.CharField(max_length=60)
    nome = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    telefone = PhoneNumberField(region='BR',  null=True, blank=True)
    data_nascimento = models.DateField(("Date"), auto_now=False, auto_now_add=False)
    data_contracacao = models.DateTimeField(("Date"), auto_now=False, auto_now_add=False)
    #relacionamento com a tabelas disciplina 
    disciplinas_atribuidas = models.CharField(max_length=100)

    def __str__(self):
        return self.nome    

class Disciplina(models.Model):
    nome = models.CharField(max_length=30)
    curso = models.CharField(max_length=30)
    carga_horaria = models.IntegerField(help_text="carga horaria em horas")
    descricao = models.CharField(max_length=40)
    professor_responsavel = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Reserva (models.Model):
    PERIODO_CHOICES = (
        ('Manhã', 'Manhã'),
        ('Tarde', 'Tarde'),
        ('Noite','Noite'),
    )

    data_inicio = models.DateField()    
    data_termino = models.DateField()
    periodo = models.CharField(max_length=10, choices=PERIODO_CHOICES)
    sala_reservada = models.CharField(max_length=40)

    ##como esta pedindo,professor responsavel e disciplina associada estão ligados como chave estrangeira Foreign Key
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina_associada = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sala_reservada} - {self.periodo}'