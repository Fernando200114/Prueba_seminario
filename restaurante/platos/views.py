from rest_framework import viewsets
from rest_framework.response import Response
from .models import Plato
from .serializers import PlatoSerializer

class PlatosViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
