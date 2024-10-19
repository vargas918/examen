from rest_framework.viewsets import ModelViewSet
from apps.preparacion.models import Preparacion
from apps.preparacion.api.serializers import PreparacionSerializer
from apps.preparacion.api.permissions import IsAdminOrReadOnly

class PreparacionModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class= PreparacionSerializer
    queryset = Preparacion.objects.all()