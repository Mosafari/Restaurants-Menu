from django.shortcuts import render, HttpResponse,HttpResponseRedirect

from django.urls import reverse_lazy, reverse 
from django.views import View

from django.contrib.auth.models import update_last_login
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
# logout user
from django.contrib.auth import logout

from .models import User, Menu

# Authentication
from django.contrib.auth import authenticate

# Create your views here.
from .forms import CustomUserCreationForm, MenuForm

# API JWT
from .serializers import MenuSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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
            print(request.user,user.is_authenticated)
            return HttpResponseRedirect(reverse('main'))
        
        
@login_required(login_url="/restaurant/login/",) 
def main(request):
    if request.method == "GET": 
        user = request.user
        return render(request, 'main.html',{'current_user': user},status=200)
    
@login_required(login_url="/restaurant/login/",) 
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required(login_url="/restaurant/login/",) 
def profile(request):
    email = request.user
    u= User.objects.filter(email=email)
    Rname = u[0].restaurant
    return render(request, 'profile.html', {'current_user': email, 'Rname': Rname}, status=200)

# add records to home page
@login_required(login_url="/restaurant/login/",) 
def home(request):
    if request.method == 'GET':
        print(request.user)
        user = User.objects.filter(email=request.user)
        name = user[0].restaurant
        results = Menu.objects.filter(restaurant_id = user[0].id)
        print(results[0].image.url,type(results[0].image.url))
        return render(request, 'home.html', {'current_user': request.user, 'name': name, 'results' : results}, status=200)

@login_required(login_url="/restaurant/login/",) 
def AddToMenu(request):
    if request.method == "GET":
        return render(request, 'edit.html', {'current_user': request.user, "form": MenuForm(None, None)})
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        print(form.files)
        if form.is_valid():
            data = form.data
            menuobj = Menu.objects.create(name = data["name"], price = float(data["price"]), categories = data["categories"], details = data["details"], restaurant = request.user, image=form.files["image"])
            menuobj.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('add'))
        
@login_required(login_url="/restaurant/login/",)  
def edit(request):
    if request.method == "GET":
        user = User.objects.filter(email=request.user)
        name = user[0].restaurant
        results = Menu.objects.filter(restaurant_id = user[0].id)
        return render(request, 'menuedit.html', {'current_user': request.user, 'name': name, 'results' : results}, status=200)
    
    if request.method == "POST":
        if request.POST.get('checkbox'):
            for i in request.POST['checkbox']:
                Menu.objects.get(id = int(i)).delete()
            for rec in Menu.objects.all():
                rec.save()
            return HttpResponseRedirect(reverse('home'))
        else :
            num = 0
            data = dict(request.POST)
            form = dict(MenuForm(request.POST, request.FILES).files)
            print(form.get("image"),data,request.POST)
            print(float(data.get('price')[num]))
            for obj in Menu.objects.filter(restaurant_id = User.objects.filter(email=request.user)[0].id):
                obj.name = data.get('name')[num]
                obj.price = float(data.get('price')[num])
                obj.categories = data.get('categories')[num]
                obj.details = data.get('details')[num]
                try:
                    if data.get(str(num)):
                        print(data.get(str(num)),form.get("image"))
                        obj.image = form.get("image").pop(0)
                except IndexError:
                    continue
                obj.save()
                num += 1
            return HttpResponseRedirect(reverse('home'))


# view for adding to menu
class AddAPI(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = MenuSerializer(data=request.data,
    context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
# show menu list of current user
from django.http import JsonResponse
class APIMenu(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        result = {}
        for num,rec in enumerate(Menu.objects.filter(restaurant_id = User.objects.filter(email=request.user)[0].id)):
            result[num+1] ={'name': rec.name,
                            'price': rec.price,
                            'details': rec.details,
                            'categories': rec.categories
                            }
        return JsonResponse(result)
            
        