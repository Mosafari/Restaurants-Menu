from django.shortcuts import render,HttpResponse

from django.urls import reverse_lazy
from django.views import View

from django.contrib.auth.models import User


# Create your views here.
class SignUpView(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            return HttpResponse(render(request, 'signup.html'), 200)
        

        