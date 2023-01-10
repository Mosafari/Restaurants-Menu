from django.shortcuts import render, HttpResponse,HttpResponseRedirect

from django.urls import reverse_lazy, reverse 
from django.views import View

from django.contrib.auth.models import update_last_login
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required

from .models import User

# Authentication
from django.contrib.auth import authenticate

# Create your views here.
from .forms import CustomUserCreationForm
class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm() 
        return render(request, 'signup.html',{'message':'Password must contain at least 8 characters.(Number\'s and Letter\'s\')', "form":form},status=200)
    
    # importing new form
    def post(self, request, *args, **kwargs):
        messages =[]
        email = request.POST.get('email')
        restaurant = request.POST.get('restaurant')
        password = request.POST.get('password1')
        print(password,email,restaurant)
        form = CustomUserCreationForm(request.POST)
        print(form.is_valid(),form.cleaned_data)
        if form.errors.as_text():
            errors = form.errors.as_text().splitlines()[1:]
            print(errors)
        else: errors = ''
        # see if restaurant already exists
        if User.objects.filter(restaurant=restaurant):
            messages.append('Restaurant\'s Name already exists')
        # see if email already exist
        if User.objects.filter(email=email).exists():
            messages.append('Email already exists')
        # if error or message is not None return to signup
        if messages or errors :
            f = CustomUserCreationForm()
            return render(request, 'signup.html',{'messages': messages, 'errors': errors, "form": f})
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request,user)
            update_last_login(None, user)
            return HttpResponseRedirect(reverse('main'))
        else:
            return render(request, 'signup.html',{'messages': ["Somthings went wrong :("], "form": f})
        
class LogInView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html',status=200)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is None:
            return render(request, 'login.html',{'messages':['Invalid Username or Password']})
        else:
            login(request,user)
            update_last_login(None, user)
            print(request.user)
            return HttpResponseRedirect(reverse('main'))
        
        
@login_required(login_url="/restaurant/login/",) 
def main(request):
    if request.method == "GET":
        return render(request, 'hello.html',status=200)
    
        