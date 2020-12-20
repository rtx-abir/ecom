from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import CustomUser
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
        return JsonResponse({'ERROR': 'Post Request only ( Email and Password)'})
    
    email = request.POST['email']
    password = request.POST['password']

#email-password validation
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        return JsonResponse({'ERROR': 'Email-type is not valid'})
    
    if len(password < 4):
        return JsonResponse({'ERROR': 'password needs a minimum of 4 characters'})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email = email)                     #checking if theres a user with that email in the DB
        
        if user.check_password(password):                               #checking for valid password
            user_dict=UserModel.objects.filter(                         # getting a dict for that user filtered with email
            email=email).values().first()          
            user_dict.pop('password')                                   # keeping every json except password to stop frontend from getting it
        
            #session validation
            if user.session_token != '0':                               #default is 0, so if not 0 a token already exists        
                user.session_token = '0'                                #setting it to 0 if not 0
                user.save()
                return JsonResponse({'ERROR': 'Session already exists'})

            token = generate_session_token()
            user.session_token = token                                  #giving the user a new session token
            user.save()
            login(request,user)                                         #with everything prepared, login attempt
            return JsonResponse({'token': token, 'user': user_dict})    #json shows token and user info except PW
        
        else:
            return JsonResponse({'Error': 'invalid password'})            # pw validation failed
    except UserModel.DoesNotExist:
        return JsonResponse({'Error': 'invalid email'})                   # email validation failed


def signout(request, id):
    

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk = id)
        user.session_token = '0'                                         # setting session token to 0 on logout
        user.save()
        logout(request)

    except UserModel.DoesNotExist:
        return JsonResponse({'ERROR': 'invalid user ID'})

    return JsonResponse({'Success': 'Logout success'})


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create':[AllowAny]}

    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]