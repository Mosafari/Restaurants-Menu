from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from django.urls import reverse_lazy
from django.views import View

from .models import User


# Create your views here.
from .forms import CustomUserCreationForm
class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()     
        return HttpResponse(render(request, 'signup.html',{'form':form}), 200)
    
    # importing new form
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        restaurant = request.POST.get('restaurant')
        password = request.POST.get('password')
        print(password,email,restaurant)
        model = User(email=email, password=password, restaurant=restaurant)
        model.save()
        return HttpResponse(render(request, 'hello.html'), 200)
        # form = CustomUserCreationForm(request.POST)
        # # check whether it's valid:
        # if form.is_valid():
        #     print(form.cleaned_data)
        #     return HttpResponse(render(request, 'hello.html'), 200)