from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import CategorySerializer
from .models import Category

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    #model viewset by default comes with list,retrieve, create, update, partial update destroy
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

    # @action(methods = ['get'], detail = False)
    # def last(self,request):
    #     query= self.get_queryset().order_by('description').last()
    #     serializer = self.get_serializer_class()(query)
    #     return Response(serializer.data)

