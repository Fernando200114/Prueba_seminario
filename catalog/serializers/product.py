# catalog/serializers/product.py
from rest_framework import serializers
from catalog.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")
    category_id = serializers.PrimaryKeyRelatedField(
        source="category", queryset=Category.objects.all(), write_only=True
    )

    class Meta:
        model = Product
        fields = ("id","codigo","name","description","categoria","is_active",
                  "category_id","category_name","created_at","updated_at")
        read_only_fields = ("id","created_at","updated_at","category_name")







   codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)
    tiempo_preparacion_min = models.IntegerField()
    calorias = models.IntegerField()
    es_vegetariano = models.BooleanField(default=False)
    nivel_picante = models.IntegerField()

    def __str__(self):