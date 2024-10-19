from rest_framework.serializers import ModelSerializer
from apps.detalles.models import Detalle_Pedido

class DetalleSerializer(ModelSerializer):
    class Meta:
        model = Detalle_Pedido
        fields = '__all__'