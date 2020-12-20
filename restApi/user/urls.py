from rest_framework import routers
from django.urls import path,include

from .views import UserViewSet, signin, signout


router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('signin/', signin, name = 'signin'),
    path('signout/<int:id>/', signout, name = 'signout')
]