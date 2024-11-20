from django.db import models

class DatosProtegido(models.Model):
    primer_nombre = models.CharField(max_length=70)
    segundo_nombre = models.CharField(max_length=70)
    primer_apellido = models.CharField(max_length=70)
    segundo_apellido = models.CharField(max_length=70)

    lider_asignado = models.CharField(max_length=255, null=True, blank=True) # pendiente por revisar
    departamento = models.PositiveSmallIntegerField()
    municipio = models.PositiveIntegerField() 
    cedula = models.CharField(max_length=11, blank=True, null=True)
    enlace_ponal = models.CharField(max_length=255, null=True, blank=True) # pendiente por revisar
    tipo_ruta = models.PositiveSmallIntegerField() #choices=[(1, 'Tipo 1'), (2, 'Tipo 2')]

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    id_protegido = models.ForeignKey(DatosProtegido, related_name='contactos', on_delete=models.CASCADE)
    contacto = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return f'Contacto de {self.id_protegido.nombre}'


class Placa(models.Model):
    id_protegido = models.ForeignKey(DatosProtegido, related_name='placas', on_delete=models.CASCADE)
    placa = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.placa
