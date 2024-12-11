from django.db import models

# Tabla estado_sicp
class EstadoSicp(models.Model):
    id_estadosicp = models.AutoField(primary_key=True)
    estado_sicp = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.estado_sicp


# Tabla departamento
class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.departamento


# Tabla municipio
class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    id_departamento = models.ForeignKey(
        Departamento, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='municipios', 
        db_column='id_departamento'
    )
    municipio = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.municipio


# Tabla parentesco
class Parentesco(models.Model):
    id_parentesco = models.AutoField(primary_key=True)
    parentesco = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return self.parentesco

# Tabla datos_protegido
class DatosProtegido(models.Model):
    id_datosprotegido = models.AutoField(primary_key=True)
    cronos = models.CharField(max_length=70, null=True, blank=True)
    tipo_documento = models.IntegerField(null=True, blank=True)
    nuip = models.IntegerField(null=True, blank=True)
    fecha_expedicion = models.CharField(max_length=10, null=True, blank=True)
    primer_nombre = models.CharField(max_length=70, null=True, blank=True)
    segundo_nombre = models.CharField(max_length=70, null=True, blank=True)
    primer_apellido = models.CharField(max_length=70, null=True, blank=True)
    segundo_apellido = models.CharField(max_length=70, null=True, blank=True)
    correo_electronico = models.CharField(max_length=70, null=True, blank=True)
    esta_activo = models.BooleanField(default=True)
    departamento = models.ForeignKey(
        Departamento, on_delete=models.SET_NULL, null=True, blank=True, db_column="departamento_id"
    )
    estado = models.ForeignKey(
        EstadoSicp, on_delete=models.SET_NULL, null=True, blank=True, db_column="estado_id"
    )
    municipio = models.ForeignKey(
        Municipio, on_delete=models.SET_NULL, null=True, blank=True, db_column="municipio_id"
    )


# Tabla Esquema
class Esquema(models.Model):
    id_esquema = models.AutoField(primary_key=True)
    tipo_ruta = models.IntegerField(null=True, blank=True)
    resolucion = models.CharField(max_length=25, null=True, blank=True)
    resuelve = models.TextField(null=True, blank=True)
    id_datosprotegido = models.ForeignKey(
        DatosProtegido,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="esquemas"
    )

    def __str__(self):
        return f"Esquema {self.id_esquema}"


# Tabla vehiculo
class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    id_esquema = models.ForeignKey(Esquema, on_delete=models.SET_NULL, null=True, blank=True, related_name='vehiculos', db_column="id_esquema")
    placa = models.CharField(max_length=6, null=True, blank=True)
    marca = models.ForeignKey('MarcaVehiculo', on_delete=models.SET_NULL, null=True, blank=True, related_name='vehiculos', db_column="marca")
    tipo = models.ForeignKey('TipoVehiculo', on_delete=models.SET_NULL, null=True, blank=True, related_name='vehiculos', db_column="tipo")
    color = models.ForeignKey('ColorVehiculo', on_delete=models.SET_NULL, null=True, blank=True, related_name='vehiculos', db_column="color")
    esta_activo = models.BooleanField(default=True)

    def __str__(self):
        return self.placa


# Tabla marca_vehiculo
class MarcaVehiculo(models.Model):
    id_marcavehiculo = models.AutoField(primary_key=True)
    marca_vehiculo = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return self.marca_vehiculo


# Tabla tipo_vehiculo
class TipoVehiculo(models.Model):
    id_tipovehiculo = models.AutoField(primary_key=True)
    tipo_vehiculo = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.tipo_vehiculo


# Tabla color_vehiculo
class ColorVehiculo(models.Model):
    id_colorvehiculo = models.AutoField(primary_key=True)
    color_vehiculo = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.color_vehiculo


# Tabla contacto
class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    id_datosprotegido = models.ForeignKey(DatosProtegido, on_delete=models.SET_NULL, null=True, blank=True, related_name='contactos', db_column="id_datosprotegido")
    contacto = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.contacto)


# Tabla persona_proteccion
class PersonaProteccion(models.Model):
    id_personaproteccion = models.AutoField(primary_key=True)
    id_esquema = models.ForeignKey(Esquema, on_delete=models.SET_NULL, null=True, blank=True, related_name='personas_proteccion', db_column="id_esquema")
    primer_nombre = models.CharField(max_length=70, null=True, blank=True)
    segundo_nombre = models.CharField(max_length=70, null=True, blank=True)
    primer_apellido = models.CharField(max_length=70, null=True, blank=True)
    segundo_apellido = models.CharField(max_length=70, null=True, blank=True)
    tipo_documento = models.IntegerField(null=True, blank=True)
    nuip = models.BigIntegerField(null=True, blank=True) 
    fecha_expedicion = models.CharField(max_length=10, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    esta_activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido}"


# Tabla familiar
class Familiar(models.Model):
    id_familiar = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=70, null=True, blank=True)
    segundo_nombre = models.CharField(max_length=70, null=True, blank=True)
    primer_apellido = models.CharField(max_length=70, null=True, blank=True)
    segundo_apellido = models.CharField(max_length=70, null=True, blank=True)
    id_datosprotegido = models.ForeignKey(DatosProtegido, on_delete=models.SET_NULL, null=True, blank=True, related_name='familiares')
    id_parentesco = models.ForeignKey(Parentesco, on_delete=models.SET_NULL, null=True, blank=True, related_name='familiares')

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido}"