# Generated by Django 5.1.2 on 2024-10-17 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_animal', '0010_animalito_descripcion_veterinario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalito',
            name='estado',
            field=models.CharField(blank=True, choices=[('calle', 'En la calle'), ('hogar_paso', 'En hogar de paso'), ('revisado_veterinario', 'Revisado por el veterinario')], default='calle', max_length=20, null=True),
        ),
    ]