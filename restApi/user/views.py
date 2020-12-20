from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomerUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout

import random
import string
import re

# Create your views here.
def generate_session_token(length = 10):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for i in range(length))

@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'ERROR: Post Request only ( Email and Password)'})
    
    email = request.POST['email']
    password = request.POST['password']

#email-password validation
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        return JsonResponse({'ERROR: Email-type is not valid'})
    
    if len(password < 4):
        return JsonResponse({'ERROR: password needs a minimum of 4 characters'})

    UserModel = get_user_model()


