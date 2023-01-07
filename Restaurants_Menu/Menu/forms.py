from django import forms
from .models import User    

class ApplicationForm(forms.ModelForm): 
    name = forms.CharField(label='Name', max_length=50) 
    restaurant = forms.CharField(label='Restaurant', max_length=50) 
    email = forms.EmailField(max_length = 254)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
    