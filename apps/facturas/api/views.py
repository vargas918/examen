from rest_framework.viewsets import ModelViewSet
from apps.facturas.models import Facturas
from apps.facturas.api.serializers import FacturaSerializer
from apps.facturas.api.permissions import IsAdminOrReadOnly

class FacturaModelViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class= FacturaSerializer
    queryset = Facturas.objects.all()