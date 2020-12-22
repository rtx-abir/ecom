from django.db import models

from restApi.category.models import Category

# Create your models here.
class product(models.Model):
    # category = models.ForeignKey(Category, on_delete = models.SET_NULL, blank= True, null= True)
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    is_active = models.BooleanField(default=True, blank= True)
    stock = models.IntegerField()
    image = models.ImageField(upload_to = "images/", blank = True, null = True)   # creates new folder inside media in settings.py
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name