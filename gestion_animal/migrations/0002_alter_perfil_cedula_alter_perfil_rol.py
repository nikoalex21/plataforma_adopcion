# Generated by Django 5.1.2 on 2024-10-17 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_animal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cedula',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='rol',
            field=models.CharField(max_length=50),
        ),
    ]
