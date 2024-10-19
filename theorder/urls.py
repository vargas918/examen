from django.contrib import admin
from django.urls import path,include
from apps.pedidos.api.router import router_pedido
from apps.productos.api.router import router_productos
from apps.detalles.api.router import router_detalles
from apps.facturas.api.router import router_factura
from apps.preparacion.api.router import router_preparacion
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pedido/',include(router_pedido.urls)),
    path('productos/',include(router_productos.urls)),
    path('detalles/',include(router_detalles.urls)), 
    path('factura/',include(router_factura.urls)),
    path('api/',include(router_preparacion.urls)),

      

    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
