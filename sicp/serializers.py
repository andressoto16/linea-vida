
from rest_framework import serializers
from sicp.models import DatosProtegido, Contacto, Placa

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'

class PlacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placa
        fields = '__all__'

class DatosProtegidoSerializer(serializers.ModelSerializer):
    contactos = ContactoSerializer(many=True)
    placas = PlacaSerializer(many=True)      

    class Meta:
        model = DatosProtegido
        fields = '__all__'

    def create(self, validated_data):

        contactos_data = validated_data.pop('contactos')
        placas_data = validated_data.pop('placas')
        
        protegido = DatosProtegido.objects.create(**validated_data)
        
        for contacto_data in contactos_data:
            Contacto.objects.create(id_protegido=protegido, **contacto_data)
        
        for placa_data in placas_data:
            Placa.objects.create(id_protegido=protegido, **placa_data)
        
        return protegido