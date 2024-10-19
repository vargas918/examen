from rest_framework.routers import DefaultRouter
from apps.detalles.api.views import DetalleModelViewset

router_detalles = DefaultRouter()
router_detalles.register(prefix="detalles",basename="detalles",viewset=DetalleModelViewset)