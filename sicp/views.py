from rest_framework import viewsets
from sicp.models import DatosProtegido
from sicp.serializers import DatosProtegidoSerializer

class DatosProtegidoViewSet(viewsets.ModelViewSet):
    queryset = DatosProtegido.objects.all()
    serializer_class = DatosProtegidoSerializer