# Generated by Django 2.2.4 on 2020-03-08 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('militares', '0003_auto_20200307_2326'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Compañias',
            new_name='Compañia',
        ),
        migrations.RenameModel(
            old_name='Servicios',
            new_name='Servicio',
        ),
        migrations.RenameModel(
            old_name='Soldados',
            new_name='Soldado',
        ),
        migrations.RenameModel(
            old_name='Soldados_registrados',
            new_name='Soldados_registrado',
        ),
    ]
