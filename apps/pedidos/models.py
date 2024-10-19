from django.db import models


class Pedidos(models.Model):

    OBSERVACIONES_CHOICES = [
        ('sin salsas', 'Sin Salsas'),
        ('sin salsa blanca', 'Sin Salsa Blanca'),
        ('con mostaza', 'Con Mostaza'),
        ('sin salsa roja', 'Sin Salsa Roja'),  
        ('sin mostaza', 'Sin Mostaza'),  
        ('sin cebolla', 'Sin Cebolla'),  
        ('sin pepinillos', 'Sin Pepinillos'),  
        ('con todas las salsas', 'Con Todas las Salsas'),
        
    ]

    PARALLEVAR_CHOICES = [
        ('si', 'Sí'),
        ('no', 'No')   
    ]

    ESTADO_CHOICES = [
        ('en espera', 'En Espera'),  
        ('en preparacion', 'En Preparación'),
        ('terminado', 'Terminado'),
    ]

  
    nombreCliente = models.CharField(max_length=50, default='Cliente Anónimo')
    cantidad = models.PositiveIntegerField(default=0)  
    llevar = models.CharField(max_length=50, choices=PARALLEVAR_CHOICES, default='no')  
    observaciones = models.CharField(max_length=50, choices=OBSERVACIONES_CHOICES,default='con todas las salsas')
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='en espera')  

    def __str__(self):
        return self.nombreCliente


