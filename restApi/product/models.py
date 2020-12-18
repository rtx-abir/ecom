from django.db import models

from restApi.category.models import Category

# Create your models here.
class product(models.Model):
    categories = models.ManyToManyField(Category)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    is_active = models.BooleanField(default=True)
    stock = models.IntegerField()
    image = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name