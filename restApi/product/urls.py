from rest_framework import routers
from django.urls import path,include

from .views import ProductViewSet
from .models import product


router = routers.DefaultRouter()
router.register(r'', ProductViewSet)

urlpatterns = [
    path('',include(router.urls))
]