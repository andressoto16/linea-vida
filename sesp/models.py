from django.db import models

# Create your models here.

class DatosSesp(models.Model):
    serial = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    cedula = models.CharField(max_length=15, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    ciudad =  models.CharField(max_length=100, blank=True, null=True)
    mtsp = models.CharField(max_length=20, blank=True, null=True)
    nivel_riesgo =  models.CharField(max_length=30, blank=True, null=True)
    telefono_contacto =  models.CharField(max_length=15, blank=True, null=True)