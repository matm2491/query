# Generated by Django 2.2.4 on 2020-03-08 00:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('militares', '0004_auto_20200308_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldado',
            name='primer_apellido',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
