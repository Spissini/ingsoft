from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class APORTE(models.Model):
    idAporte = models.IntegerField(primary_key=True, verbose_name='Numero Aporte')
    cantAporte = models.IntegerField(verbose_name='Cantidad de Aporte')
    rutAportador = models.IntegerField(verbose_name='Rut del aportador')
    nombAportador = models.CharField(max_length=15, verbose_name='Nombre del aportador')
    apeAportador = models.CharField(max_length=25, verbose_name='Apellidos del aportador')
    numTarjeta = models.IntegerField(verbose_name='Numero de la Tarjeta')
    def __str__(self):
            return self.idAporte

#class EMPRETAIL(models.Model):
#    num_Tarjeta = models.IntegerField(primary_key=True, verbose_name='Numero de Tarjeta')
#    nom_Emp = models.CharField(max_length=15, verbose_name='Nombre de la Empresa')
#    def __str__(self):
#       return self.num_Tarjeta

#class APORTADOR(models.Model):
#    rut_Aport = models.IntegerField(primary_key=True, verbose_name='Rut del Apoortador')
#    nomb_Aport = models.CharField(max_length=15, verbose_name='Nombre del Aportador')
#    apelli_Aport = models.CharField(max_length=25, verbose_name='Apellidos del Aportador')
#    num_Aport = models.IntegerField(verbose_name='Numero Telefonico del Aportador')
#    correo_Aport = models.CharField(max_length=45, verbose_name='Correo del Aportador')
#    def __str__(self):
#        return self.rut_Aport

#class APORTE(models.Model):
#    id_Aporte = models.IntegerField(primary_key=True, verbose_name='ID Del Aporte')
#    cant_Aporte = models.IntegerField(verbose_name='Cantidad del Aporte')
#    aportador = models.ForeignKey(APORTADOR, on_delete=models.CASCADE)
#    empretail = models.ForeignKey(EMPRETAIL, on_delete=models.CASCADE)
#    def __str__(self):
#        return self.id_Aporte

class residente(models.Model):
    rutResident = models.IntegerField(primary_key=True, verbose_name='Rut aporte')
    nombsResident = models.CharField(max_length=50, verbose_name='Nombre residente')
    edadResident = models.IntegerField(verbose_name='Edad residente')
    tutorResi = models.CharField(max_length=50, verbose_name='Nombre tutor')
    medicaResident = models.CharField(max_length=50, verbose_name='Medicamentos')
    saludResident = models.CharField(max_length=50, verbose_name='salud del residente')
    cuidadResident = models.CharField(max_length=50, verbose_name='Cuidados especiales')
    fichaResidente = models.ImageField(upload_to="Ficha", null = True)

    def str(self):
            return self.rutResident

class ingresos(models.Model):
    idIngreso = models.IntegerField(primary_key=True, verbose_name='Id registro de salida')
    salidaRes = models.CharField(max_length=15, verbose_name='Salida de residente')
    ingresoRes = models.CharField(max_length=15, verbose_name='Ingreso de residente')
    Residente = models.ForeignKey(residente, on_delete=models.CASCADE)

    def __str__(self):
        return self.idIngreso