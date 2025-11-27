from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PlatosViewSet

router = DefaultRouter()
router.register('platos', PlatosViewSet, basename='platos')

urlpatterns = [
    path('', include(router.urls)),  
]
