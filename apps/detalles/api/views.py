from rest_framework.viewsets import ModelViewSet
from apps.detalles.models import Detalle_Pedido
from apps.detalles.api.serializers import DetalleSerializer
from apps.detalles.api.permissions import IsAdminOrReadOnly

class DetalleModelViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class= DetalleSerializer
    queryset = Detalle_Pedido.objects.all()