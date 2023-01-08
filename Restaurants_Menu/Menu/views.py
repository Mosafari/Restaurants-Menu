from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from django.urls import reverse_lazy
from django.views import View

from .models import User

# Authentication
from django.contrib.auth import authenticate

# Create your views here.
from .forms import CustomUserCreationForm
class SignUpView(View):
    def get(self, request, *args, **kwargs): 
        return render(request, 'signup.html',status=200)
    
    # importing new form
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        restaurant = request.POST.get('restaurant')
        password = request.POST.get('password')
        print(password,email,restaurant)
        # see if restaurant already exists
        if User.objects.filter(restaurant=restaurant):
            return render(request, 'signup.html',{'message':'Restaurant\'s Name already exists'})
        # see if email already exist
        elif User.objects.filter(email=email).exists():
            return render(request, 'signup.html',{'message':'Email already exists'})
        else:
            model = User(email=email, password=password, restaurant=restaurant)
            model.save()
            return render(request, 'hello.html',status=200)
        
        
class LogInView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html',status=200)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(CustomUserCreationForm())
        user = authenticate(username=email, password=password)
        if user is None:
            print('Invalid Username or Password')
        else:
            print("Pass")
        