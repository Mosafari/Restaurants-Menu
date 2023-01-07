from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response

from .forms import ApplicationForm 
from .models import User
# signup template
class SignUpView(generic.CreateView):
    model = User
    form = ApplicationForm() 
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
    

# view for registering users
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
