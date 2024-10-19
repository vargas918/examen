from rest_framework.routers import DefaultRouter
from apps.preparacion.api.views import PreparacionModelViewSet

router_preparacion = DefaultRouter()
router_preparacion.register(prefix="preparacion",basename="preparacion",viewset=PreparacionModelViewSet)