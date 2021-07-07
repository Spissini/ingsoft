# Generated by Django 3.2.3 on 2021-07-06 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_aporte'),
    ]

    operations = [
        migrations.CreateModel(
            name='residente',
            fields=[
                ('rutResident', models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut aporte')),
                ('nombsResident', models.CharField(max_length=50, verbose_name='Nombre residente')),
                ('edadResident', models.IntegerField(verbose_name='Edad residente')),
                ('medicaResident', models.CharField(max_length=50, verbose_name='Medicamentos')),
                ('saludResident', models.CharField(max_length=50, verbose_name='salud del residente')),
                ('cuidadResident', models.CharField(max_length=50, verbose_name='Cuidados especiales')),
            ],
        ),
    ]
