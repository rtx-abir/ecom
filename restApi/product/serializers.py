from rest_framework import serializers

from .models import product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length = None, allow_empty_file = False, allow_null= True, required = False)
    class Meta:
        model = product
        fields = '__all__'
        depth = 1