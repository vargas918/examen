from rest_framework.viewsets import ModelViewSet
from apps.pedidos.models import Pedidos
from apps.pedidos.api.serializers import PedidoSerializer
from apps.pedidos.api.permissions import IsAdminOrReadOnly

class PedidoModelViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class= PedidoSerializer
    queryset = Pedidos.objects.all()