from django.db import models

class DatosProtegido(models.Model):
    nombre = models.CharField(max_length=255)
    lider_asignado = models.CharField(max_length=255, null=True, blank=True)
    departamento = models.PositiveSmallIntegerField()
    municipio = models.PositiveIntegerField() 
    cedula = models.BigIntegerField()
    enlace_ponal = models.CharField(max_length=255, null=True, blank=True)
    tipo_ruta = models.PositiveSmallIntegerField() #choices=[(1, 'Tipo 1'), (2, 'Tipo 2')]

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    id_protegido = models.ForeignKey(DatosProtegido, related_name='contactos', on_delete=models.CASCADE)
    contacto = models.BigIntegerField()

    def __str__(self):
        return f'Contacto de {self.id_protegido.nombre}'


class Placa(models.Model):
    id_protegido = models.ForeignKey(DatosProtegido, related_name='placas', on_delete=models.CASCADE)
    placa = models.CharField(max_length=6)

    def __str__(self):
        return self.placa
