from django.db import models

# Create your models here.
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from sistema import models as sis_models


##    
class pais(models.Model):
    id_pais = models.SmallAutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=170, null=True, blank=True)
    
    class Meta:
        db_table = 'eco_ext_pais'
        verbose_name_plural = 'pais'

    def __str__(self):
        return str(self.nombre_pais)

##
class departamento(models.Model):
    id_departamento = models.SmallAutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=170, null=True, blank=True)
    id_pais = models.ForeignKey(pais, to_field='id_pais', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'eco_ext_departamento'
        verbose_name_plural = 'Departamento'

    def __str__(self):
        return str(self.nombre_departamento)
    
## 
class municipio(models.Model):
    id_municipio = models.SmallAutoField(primary_key=True)
    nombre_municipio = models.CharField(max_length=170, null=True, blank=True)
    
    class Meta:
        db_table = 'eco_ext_municipio'
        verbose_name_plural = 'municipio'
        
    def __str__(self):
        return str(self.nombre_municipio)


# datos de ubicacion TH
class zonaubicacionth(models.Model):
    id_zubicacion = models.SmallAutoField(primary_key=True)
    nombre_zubicacion = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'eco_bas_zonaubicacionth'
        verbose_name_plural = 'zona de ubicacion de la persona'


class ubicacionth(models.Model):
    id_ubicacion = models.SmallAutoField(primary_key=True)
    pais_ubicacion = models.ForeignKey(pais, to_field='id_pais', on_delete=models.CASCADE)
    departamento_ubicacion = models.ForeignKey(municipio, to_field='id_departamento', on_delete=models.CASCADE)
    municipio_ubicacion = models.ForeignKey(municipio, to_field='id_municipio', on_delete=models.CASCADE)
    zona_ubicacion = models.ForeignKey(zonaubicacionth, to_field='id_zubicacion', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=160, blank=True, null=True)
    indicacion = models.CharField(max_length=160, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        db_table = 'eco_esp_ubicacionth'
        verbose_name_plural = 'Datos de ubicación'

    def __str__(self):
        return str(self.id_ubicacion)

class direccionurbanath(ubicacionth):
    nombre_barrio = models.CharField(max_length=100)
    tipo_viaprincipal = models.CharField(max_length=20)
    numero_viaprincipal = models.CharField(max_length=20)
    letra_viaprincipal = models.CharField(max_length=10)
    es_bis = models.BooleanField(default=False)
    letra_bis = models.CharField(max_length=10)
    cuadrante_principal = models.CharField(max_length=10)
    numero_viasecundaria = models.CharField(max_length=10)
    letra_secundaria = models.CharField(max_length=10)
    cuadrante_secundario = models.CharField(max_length=10)
    numero_placa = models.CharField(max_length=10)
    complemento = models.CharField(max_length=60)
    
    class Meta:
        db_table = 'eco_esp_direccionurbanath'
        verbose_name_plural = 'direccion urbana de la persona'
        
class direccionruralth(ubicacionth):
    corregimiento = models.CharField(max_length=150)
    centro_poblado = models.CharField(max_length=150)
    vereda = models.CharField(max_length=150)
    
    class Meta:
        db_table = 'eco_esp_direccionruralth'
        verbose_name_plural = 'direccion rural de la persona'
        
class nombreetcrth(ubicacionth):
    nombre_etcr = models.CharField(max_length=120)
    
    class Meta:
        db_table = 'eco_esp_nombreetcrth'
        verbose_name_plural = 'nombre etcr de la persona'
        
class nombrenarth(ubicacionth):
    nombre_nar = models.CharField(max_length=120)
    
    class Meta:
        db_table = 'eco_esp_nombrenarth'
        verbose_name_plural = 'nombre nar de la persona'

##
class tipoidentificacionth(models.Model):
    id_tidentificacion = models.SmallAutoField(primary_key=True)
    nombre_tidentificacion = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'eco_bas_tipoidentificacionth'
        verbose_name_plural = 'Tipo de Identificacion'
        
    def __str__(self):
        return str(self.nombre_tidentificacion)

##    
class tipogenero(models.Model):
    id_tgenero = models.SmallAutoField(primary_key=True)
    nombre_tgenero = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'eco_bas_tipogenero'
        verbose_name_plural = 'Tipo de género'

    def __str__(self):
        return str(self.nombre_tgenero)
    
##    
class tiposexo(models.Model):
    id_sexo = models.SmallAutoField(primary_key=True)
    nombre_sexo = models.CharField(max_length=30, null=True, blank=True)
    
    class Meta:
        db_table = 'eco_bas_tiposexo'

    def __str__(self):
        return str(self.nombre_sexo)

##
class tidentidadgenero(models.Model):
    id_tidentidadgenero = models.SmallAutoField(primary_key=True)
    nombre_tidentidadgenero = models.CharField(max_length=80, null=True, blank=True)
    
    class Meta:
        db_table = 'eco_bas_tidentidadgenero'
        verbose_name_plural = 'Identidad de genero'

    def __str__(self):
        return str(self.nombre_tidentidadgenero)

##
class nombrepersona(models.Model):
    id_npersona = models.SmallAutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=30, null=True, blank=True)
    segundo_nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50, null=True, blank=True)
    segundo_nombre = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'eco_esp_nombrepersonath'

    def __str__(self):
        return str(self.id_npersona)

##
class ipersonath(models.Model):
    id_ipersona = models.SmallAutoField(primary_key=True)
    numero_identificacion = models.CharField(max_length=15, null=True, blank=True)
    
    class Meta:
        db_table = 'eco_esp_ipersonath'
        verbose_name_plural = 'identificacion de la persona_th'

    def __str__(self):
        return str(self.numero_identificacion)

##
class basicospersonath(models.Model):
    id_personath = models.SmallAutoField(primary_key=True)
    nombre_personath = models.ForeignKey(nombrepersona, to_field='id_npersona', on_delete=models.CASCADE)
    identificacion_personath = models.ForeignKey(ipersonath, to_field='id_ipersona', on_delete=models.CASCADE)
    genero_personath = models.ForeignKey(tipogenero, to_field='id_tgenero', on_delete=models.CASCADE)
    sexo_personath = models.ForeignKey(tiposexo, to_field='id_sexo', on_delete=models.CASCADE)
    identidad_generoth = models.ForeignKey(tidentidadgenero, to_field='id_tidentidadgenero', on_delete=models.CASCADE)
    ubicacion_personath = models.GenericRelation(sis_models.DatosUbicacion)
    contacto_personath = models.GenericRelaction(sis_models.DatosContacto)
    
    class Meta:
        db_table = 'eco_esp_basicospersonath'
        verbose_name_plural = 'Basicos de la persona th'

    def __str__(self):
        return str(self.nombrepersona)
    

class nidentitario(models.Model):
    id_nidentitario = models.SmallAutoField(primary_key=True)
    nombre_identitario = models.CharField(max_length=30)
    basicospersonath = models.ForeignKey(basicospersonath, to_field='id_persona', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_esp_nidentitarioth'
        verbose_name_plural = 'Nombre Identitario de la persona'

    def __str__(self):
        return str(self.nombre_identitario)


class nacimientopersona(models.Model):
    id_dnacimiento = models.SmallAutoField(primary_key=True)
    pais_ubicacion = models.ForeignKey(pais, to_field='id_pais', on_delete=models.CASCADE)
    departamento_ubicacion = models.ForeignKey(municipio, to_field='id_departamento', on_delete=models.CASCADE)
    municipio_ubicacion = models.ForeignKey(municipio, to_field='id_municipio', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_esp_nacimientopersonath'
        verbose_name_plural = 'Datos de nacimiento de la persona'

    def __str__(self):
        return str(self.id_dnacimiento)


class TelefonoCelularContacto(models.Model):
    id_ctelefono = models.SmallAutoField(primary_key=True)
    celular_uno = models.CharField(max_length=15, blank=True, null=True)
    celular_dos = models.CharField(max_length=15, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'eco_sis_ctelefono'
        verbose_name_plural = 'Datos de contacto'

    def __str__(self):
        return str(self.id_ctelefono)
    
class CorreoElectronicoContacto(models.Model):
    id_ccelectronico = models.SmallAutoField(primary_key=True)
    correo_electronico = models.EmailField(max_length=100)
    autoriza_envio = models.BooleanField(default=False)

    class Meta:
        db_table = 'eco_esp_ccelectronico'
        verbose_name_plural = 'Datos de contacto'

    def __str__(self):
        return str(self.id_ccelectronico)
    
class DatosContacto(models.Model):
    id_contacto = models.SmallAutoField(primary_key=True)
    id_ctelefono = models.ForeignKey(TelefonoCelularContacto, to_field='id_ctelefono', on_delete=models.CASCADE)
    id_ccelectronico = models.ForeignKey(CorreoElectronicoContacto, to_field='id_ccelectronico', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'eco_esp_contacto'
        verbose_name_plural = 'Datos de contacto'

    def __str__(self):
        return str(self.id_contacto)

# Datos Complementarios
class estadocivilth(models.Model):
    id_ecivil = models.SmallAutoField(primary_key=True)
    nombre_ecivil = models.CharField(max_length=80, null=True, blank=True)
    
    class Meta:
        db_table = 'eco_esp_estadocivilth'
        verbose_name_plural = 'Estado Civil de la persona'
    def __str__(self):
        return str(self.id_ecivil)
    
class nescolaridadth(models.Model):
    id_nescolaridad = models.SmallAutoField(primary_key=True)
    nombre_nescolaridad = models.CharField(max_length=80, null=True, blank=True)
    
    class Meta:
        db_table = 'eco_esp_nescolaridadth'
        verbose_name_plural = 'Nivel de escolaridad'
    def __str__(self):
        return str(self.id_nescolaridad)
    
class grupoindigenath(models.Model):
    id_gindigenath = models.SmallAutoField(primary_key=True)
    etnia = models.CharField(max_length=100, null=True, blank=True)
    resguardo = models.CharField(max_length=100)
    comunidad = models.CharField(max_length=100)
    parcialidad = models.CharField(max_length=100)
    comunidad_sregistro = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'eco_esp_grupoindigenath'
        verbose_name_plural = 'Grupo Indígena de la persona'
    def __str__(self):
        return str(self.id_gindigenath)

class tipoetnicoth(models.Model):
    id_tipoetnicoth = models.SmallAutoField(primary_key=True)
    nombre_tipoetnicoth = models.CharField(max_length=80, null=True, blank=True)
    
    class Meta:
        db_table = 'eco_esp_tipoetnicoth'
        verbose_name_plural = 'Tipo Etnico de la persona'
    def __str__(self):
        return str(self.id_tipoetnicoth)

class grupoetnicoth(models.Model):
    id_getnicoth = models.SmallAutoField(primary_key=True)
    tipo_etnicoth = models.ForeignKey(tipoetnicoth, to_field='id_tipoetnicoth' , on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'eco_esp_grupoetnicoth'
        verbose_name_plural = 'Grupo Etnico de la persona'
    def __str__(self):
        return str(self.id_getnicoth)
    
class etnicoindigena(models.Model):
    id_etnicoindigena = models.SmallAutoField(primary_key=True)
    grupoetnicoth = models.ForeignKey(grupoetnicoth, to_field='id_getnicoth', on_delete=models.CASCADE)
    grupoindigenath = models.ForeignKey(grupoindigenath, to_field='id_gindigenath')

    class Meta:
        db_table = 'eco_esp_etnicoindigenath'
        verbose_name_plural = 'Etnico Indígena de la persona'
    def __str__(self):
        return str(self.id_etnicoindigena)
    
class ogetnicoth(models.Model):
    id_ogetnicoth = models.SmallAutoField(primary_key=True)
    nombre_ccomunitario = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'eco_esp_ogetnicoth'
        verbose_name_plural = 'Otro Etnico de la persona'
    def __str__(self):
        return str(self.id_ogetnicoth)


class etnicoconsejoth(models.Model):
    id_etnicoconsejoth = models.SmallAutoField(primary_key=True)
    etnicoconcejo_grupoetnicoth = models.ForeignKey(grupoetnicoth, to_field='id_getnicoth', on_delete=models.CASCADE)
    otro_grupo = models.ForeignKey(ogetnicoth, to_field='id_ogetnicoth', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'eco_esp_etnicoconsejoth'
        verbose_name_plural = 'Etnico Consejo de la persona'
        def __str__(self):
            return str(self.id_etnicoconsejoth)

        
class tipodiscapacidadth(models.Model):
    id_tipodiscapacidadth = models.SmallAutoField(primary_key=True)
    nombre_tipodiscapacidad = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'eco_esp_tipodiscapacidadth'
        verbose_name_plural = 'Tipo de discapacidad de la persona'
        
    def __str__(self):
        return str(self.id_tipodiscapacidadth)
    

class discapacidadpersonath(models.Model):
    id_dpersona = models.SmallAutoField(primary_key=True)
    tipo_discapacidad = models.ForeignKey(tipodiscapacidadth, to_field='id_tipodiscapacidadth', on_delete=models.CASCADE)
    cpersonath = models.ForeignKey(cpersonath, to_field='id_cpersona', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'eco_esp_discapacidadpersonath'
        verbose_name_plural = 'Discapacidad de la persona'
    def __str__(self):
        return str(self.id_dpersona)
    
 
class rangoetarioth(models.Model):
    id_rangoetarioth = models.SmallAutoField(primary_key=True)
    nombre_rangoetario = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'eco_bas_rangoetarioth'
        verbose_name_plural = 'Rango etario de la persona'
    def __str__(self):
        return str(self.id_rangoetarioth)
    
class tipofdiferencialth(models.Model):
    id_tipofdiferencial = models.SmallAutoField(primary_key=True)
    nombre_tipofdiferencial = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'eco_bas_tipofdiferencial'
        verbose_name_plural = 'Tipo de diferencia de la persona'
    def __str__(self):
        return str(self.id_tipofdiferencial)


class cpersonath(models.Model):
    id_cpersonath = models.SmallAutoField(primary_key=True)
    estado_civil = models.ForeignKey(estadocivilth, to_field='id_ecivil', on_delete=models.CASCADE)
    nivel_escolaridad = models.ForeignKey(nescolaridadth, to_field='id_nescolaridad', on_delete=models.CASCADE)
    pertenece_getnico = models.BooleanField(default=False)
    tiene_discapacidad = models.BooleanField(default=False)
    tiene_sexequial = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'eco_esp_compersonath'
        verbose_name_plural = 'Datos complementarios de la persona'
    def __str__(self):
        return str(self.id_cpersonath)

class ltrabajopersonath(models.Model):
    id_ltrabajopersonath = models.SmallAutoField(primary_key=True)
    ltrabajo_pais = models.ForeignKey(pais, to_field='id_pais', on_delete=models.CASCADE)
    ltrabajo_municipio = models.ForeignKey(municipio, to_field='id_municipio', on_delete=models.CASCADE)
    ltrabajo_departamento = models.ForeignKey(departamento, to_field='id_departamento', on_delete=models.CASCADE)
    ltrabajo_zona = models.ForeignKey(zonaubicacionth, to_field='id_zonaubicacionth', on_delete=models.CASCADE)
    id_cpersona = models.ForeignKey(cpersonath, to_field='id_cpersona', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'eco_esp_ltrabajopersonath'
        verbose_name_plural = 'Lugar de trabajo de la persona'
        def __str__(self):
            return str(self.id_ltrabajopersonath)
        
class factordiferencialth(models.Model):
    id_factordiferencialth = models.SmallAutoField(primary_key=True)
    tipo_factordiferencial = models.ForeignKey(tipofdiferencialth, to_field='id_tipofdiferencial', on_delete=models.CASCADE)
    id_cpersona = models.ForeignKey(cpersonath, to_field='id_cpersona', on_delete=models.CASCADE)
    
    class Meta: 
        db_table = 'eco_esp_fdiferencial'
        verbose_name_plural = 'Factor de diferencia de la persona'
    def __str__(self):
        return str(self.id_factordiferencialth)
    
class numeropersonasacargoth(models.Model):
    id_numeropcargo = models.SmallAutoField(primary_key=True)
    tipo_etariodiferencial = models.ForeignKey(tipofdiferencialth)
    cantidad_personas = models.IntegerField()
    id_ofdiferencial = models.ForeignKey()
    
    class Meta:
        db_table = 'eco_esp_numeropersonasacargoth'
        verbose_name_plural = 'Número de personas a cargo de la persona'
    def __str__(self):
        return str(self.id_familiapcargo)

class personascargoth(models.Model):
    id_pcargo = models.SmallAutoField(primary_key=True)
    numero_pcargo = models.ForeignKey(numeropersonasacargoth, to_field='id_numeropcargo', on_delete=models.CASCADE)
    factor_diferencial = models.ForeignKey(factordiferencialth, to_field='id_factordiferencialth', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'eco_esp_personascargoth'
        verbose_name_plural = 'Persona a cargo de la persona'
    def __str__(self):
        return str(self.id_pcargo)

#Datos del formulario TH
class ldiligenciath(models.Model):
    id_ldiligencia = models.SmallAutoField(primary_key=True)
    pais_ldiligencia = models.ForeignKey(pais, to_field='id_pais', on_delete=models.CASCADE)
    departamento_ldiligencia = models.ForeignKey(departamento, to_field='id_departamento', on_delete=models.CASCADE)
    municipio_ldiligencia = models.ForeignKey(municipio, to_field='id_municipio', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'eco_esp_ldiligencia'
        verbose_name_plural = 'Lugar de la diligenciamiento'
    def __str__(self):
        return str(self.id_ldiligencia)
    
class rolth(models.Model):
    id_rolth = models.SmallAutoField(primary_key=True)
    esquema = models.CharField(max_length=150)
    tiempo_entidad = models.DateField()
    tiempo_rol = models.DateField()
    rol = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'eco_esp_rolth'
        verbose_name_plural = 'Rol que desempeña'
    def __str__(self):
        return str(self.id_rolth)
    
class formularioth(models.Model):
    id_formularioth = models.SmallAutoField(primary_key=True)
    rol = models.ForeignKey(rolth, to_field='id_rolth', on_delete=models.CASCADE)
    lugar_diligencia = models.ForeignKey(ldiligenciath, to_field='id_ldiligencia', on_delete=models.CASCADE)
    id_persona = models.ForeignKey(basicospersonath, to_field='id_personath', on_delete=models.CASCADE)
    id_cpersona = models.ForeignKey()