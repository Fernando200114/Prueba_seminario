# catalog/models/product.py
from django.db import models


class Plato(models.Model):
    codigo = models.CharField(max_length=160)
    nombre = models.CharField(max_length=160)
    descripcion = models.TextField()
    categoria =  models.CharField(max_length=160)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    tiempo_preparacion_min = models.IntegerField()
    calorias = models.IntegerField()
    es_vegetariano = models.BooleanField(default=True)
    nivel_picante = models.IntegerField()


    def __str__(self):
        return self.name
