from django.db import models

class Productos(models.Model):
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_producto = models.DecimalField(max_digits=10, decimal_places=3 ,default=0)
     

    def __str__(self):
        return self.nombre_producto

