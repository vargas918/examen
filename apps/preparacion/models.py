from django.db import models
from apps.pedidos.models import Pedidos
from apps.productos.models import Productos
from apps.detalles.models import Detalle_Pedido

# Create your models here.
class Preparacion(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Productos, on_delete=models.SET_NULL, null=True)
    cantidad = models.ForeignKey(Detalle_Pedido, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=20, choices=[
        ('En espera', 'En espera'),
        ('En preparación', 'En preparación'),
        ('Terminado', 'Terminado')
    ], default='En preparación')

    def __str__(self):
        return f"pedido:{self.pedido.nombreCliente}, producto:{self.producto.nombre_producto}, cantidad:{self.cantidad.cantidad}, Para llevar: {self.pedido.llevar}, estado:{self.estado}"

