# Generated by Django 5.2 on 2025-05-08 16:39

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('curso', models.CharField(max_length=30)),
                ('carga_horaria', models.IntegerField(help_text='carga horaria em horas')),
                ('descricao', models.CharField(max_length=40)),
                ('professor_responsavel', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ni', models.CharField(max_length=60)),
                ('nome', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=80)),
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='BR')),
                ('data_nascimento', models.DateField(verbose_name='Date')),
                ('data_contracacao', models.DateTimeField(verbose_name='Date')),
                ('disciplinas_atribuidas', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('periodo', models.CharField(choices=[('Manhã', 'Manhã'), ('Tarde', 'Tarde'), ('Noite', 'Noite')], max_length=10)),
                ('sala_reservada', models.CharField(max_length=40)),
                ('disciplina_associada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina')),
                ('professor_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.professor')),
            ],
        ),
    ]
