# Generated by Django 3.2.3 on 2021-06-15 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_delete_aporte'),
    ]

    operations = [
        migrations.CreateModel(
            name='APORTE',
            fields=[
                ('idAporte', models.IntegerField(primary_key=True, serialize=False, verbose_name='Numero Aporte')),
                ('cantAporte', models.IntegerField(verbose_name='Cantidad de Aporte')),
                ('rutAportador', models.IntegerField(verbose_name='Rut del aportador')),
                ('nombAportador', models.CharField(max_length=15, verbose_name='Nombre del aportador')),
                ('apeAportador', models.CharField(max_length=25, verbose_name='Apellidos del aportador')),
                ('numTarjeta', models.IntegerField(verbose_name='Numero de la Tarjeta')),
            ],
        ),
    ]
