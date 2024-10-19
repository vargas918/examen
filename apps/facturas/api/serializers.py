from rest_framework.serializers import ModelSerializer
from apps.facturas.models import Facturas

class FacturaSerializer(ModelSerializer):
    class Meta:
        model = Facturas
        fields = '__all__'