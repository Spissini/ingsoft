# Generated by Django 3.1.3 on 2021-06-14 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APORTADOR',
            fields=[
                ('rut_Aport', models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut del Apoortador')),
                ('nomb_Aport', models.CharField(max_length=15, verbose_name='Nombre del Aportador')),
                ('apelli_Aport', models.CharField(max_length=25, verbose_name='Apellidos del Aportador')),
                ('num_Aport', models.IntegerField(verbose_name='Numero Telefonico del Aportador')),
                ('correo_Aport', models.CharField(max_length=45, verbose_name='Correo del Aportador')),
            ],
        ),
    ]