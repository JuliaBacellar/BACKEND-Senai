# Generated by Django 5.1.7 on 2025-03-20 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciar_eventos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Evento',
        ),
    ]
