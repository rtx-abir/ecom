from django.urls import path, include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path('', home, name = 'api.home'),
    path('category/',include('restApi.category.urls')),
    path('product/' , include('restApi.product.urls')),
    path('user/' , include('restApi.user.urls'))
]