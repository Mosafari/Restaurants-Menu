from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from django.urls import reverse_lazy
from django.views import View

from .models import User


# Create your views here.
from .forms import CustomUserCreationForm
class SignUpView(View):
    def get(self, request, *args, **kwargs): 
        return HttpResponse(render(request, 'signup.html'), 200)
    
    # importing new form
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        restaurant = request.POST.get('restaurant')
        password = request.POST.get('password')
        print(password,email,restaurant)
        # see if restaurant already exists
        if User.objects.filter(restaurant=restaurant):
            return HttpResponse(render(request, 'signup.html',{'message':'Restaurant\'s Name already exists'}))
        # see if email already exist
        elif User.objects.filter(email=email).exists():
            return HttpResponse(render(request, 'signup.html',{'message':'Email already exists'}))
        else:
            model = User(email=email, password=password, restaurant=restaurant)
            model.save()
            return HttpResponse(render(request, 'hello.html'), 200)
