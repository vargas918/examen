from django.db import models
from apps.pedidos.models import Pedidos
from apps.productos.models import Productos
from apps.pedidos.models import Pedidos

# Create your models here.
class Detalle_Pedido(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.SET_NULL, null=True)
    observaciones = models.TextField(blank=True, null=True)
    cantidad = models.PositiveIntegerField()
    pedido = models.ForeignKey(Pedidos, related_name='detalles', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.cantidad} - {self.producto.nombre_producto}"
