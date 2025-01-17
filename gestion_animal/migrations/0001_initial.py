# Generated by Django 5.1.2 on 2024-10-17 16:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=20, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('rol', models.CharField(choices=[('veterinario', 'Centro Veterinario'), ('hogar_paso', 'Hogar de Paso'), ('adoptante', 'Adoptante'), ('colaborador', 'Colaborador'), ('ayudador', 'Ayudador')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
