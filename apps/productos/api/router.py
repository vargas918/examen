from rest_framework.routers import DefaultRouter
from apps.productos.api.views import ProductosModelViewSet

router_productos = DefaultRouter()
router_productos.register(prefix="productos",basename="productos",viewset=ProductosModelViewSet)