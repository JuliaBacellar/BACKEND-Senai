# Generated by Django 5.1.7 on 2025-03-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudante', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='rm',
            field=models.PositiveIntegerField(),
        ),
    ]
