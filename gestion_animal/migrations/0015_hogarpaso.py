# Generated by Django 5.1.2 on 2024-10-18 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_animal', '0014_alter_animalito_ayudador'),
    ]

    operations = [
        migrations.CreateModel(
            name='HogarPaso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
    ]
