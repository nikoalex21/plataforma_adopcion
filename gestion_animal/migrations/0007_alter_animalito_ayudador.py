# Generated by Django 5.1.2 on 2024-10-17 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_animal', '0006_animalito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalito',
            name='ayudador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_animal.perfil'),
        ),
    ]