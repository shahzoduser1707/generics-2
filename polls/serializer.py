from rest_framework import serializers
from .models import Workers,Orders

class WorkersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = ('__all__')

class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('__all__')