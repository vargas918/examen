from django.db import models
from django.db import models
from apps.pedidos.models import Pedidos
from apps.productos.models import Productos
from apps.detalles.models import Detalle_Pedido

# Create your models here.
class Facturas(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Productos, on_delete=models.SET_NULL, null=True)
    cantidad = models.ForeignKey(Detalle_Pedido, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.pedido}Total a pagar:{self.cantidad.cantidad * self.producto.precio_producto}"
