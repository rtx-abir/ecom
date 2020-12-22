from rest_framework import viewsets

from .serializers import ProductSerializer
from .models import product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all().order_by('name')
    serializer_class = ProductSerializer

# Create your views here.
