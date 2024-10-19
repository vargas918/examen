from rest_framework.serializers import ModelSerializer
from apps.preparacion.models import Preparacion

class PreparacionSerializer(ModelSerializer):
    class Meta:
        model = Preparacion
        fields = '__all__'