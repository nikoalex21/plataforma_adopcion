# Generated by Django 5.1.2 on 2024-10-18 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_animal', '0017_solicitudadopcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudadopcion',
            name='fecha_solicitud',
        ),
        migrations.AlterField(
            model_name='solicitudadopcion',
            name='direccion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='solicitudadopcion',
            name='edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='solicitudadopcion',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('aprobada', 'Aprobada'), ('rechazada', 'Rechazada')], default='pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='solicitudadopcion',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
    ]