from rest_framework import serializers
from .models import Product # type: ignore

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'