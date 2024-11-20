from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DatosProtegidoViewSet

# Crear un enrutador para las vistas
router = DefaultRouter()
router.register(r'datos-protegido', DatosProtegidoViewSet)

# Definir las rutas
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('sicp.urls')),
]