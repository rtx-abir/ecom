from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomerUser(AbstractUser):
    name = models.CharField(max_length=40, default='Annonymous')
    email = models.EmailField(max_length=200, unique=True)
    username = None

    USERNAME_FIELD = 'email'            # makes login using email rather than username
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=30, blank =True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)

    session_token = models.CharField(max_length=10,default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)