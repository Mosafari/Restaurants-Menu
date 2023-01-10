from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

from django.forms import TextInput, EmailInput , CharField, PasswordInput
from django.utils.translation import gettext_lazy as _
class CustomUserCreationForm(UserCreationForm):
    password1 = CharField(
        label=_("Password"),
        strip=False,
        widget= PasswordInput(attrs={
    'class': "input is-large",
                'placeholder': 'Password'    
    }),
    )
    password2 = CharField(
        label=_("Password confirmation"),
        widget= PasswordInput(attrs={
    'class': "input is-large",
                'placeholder': 'Confirm Password'    
    }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ('email','restaurant',)
        widgets = {
            'email' : EmailInput(attrs={
                'class': "input is-large", 
                'autofocus': '',
                'placeholder': 'Email'
                }),
            'restaurant': TextInput(attrs={
                'class': "input is-large",
                'autofocus': '',
                'placeholder': 'Restaurant\' Name'
                }),
            
        }
    def clean(self):

        # data from the form is fetched using super function
        super(CustomUserCreationForm, self).clean_password2()

    # return any errors if found
        return self.cleaned_data


class CustomUserChangeForm(UserChangeForm):
    password1 = CharField(
        label=_("Password"),
        strip=False,
        widget= PasswordInput(attrs={
    'class': "input is-large",
                'placeholder': 'Password'    
    }),
    )
    password2 = CharField(
        label=_("Password confirmation"),
        widget= PasswordInput(attrs={
    'class': "input is-large",
                'placeholder': 'Cpnfirm Password'    
    }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ('email','restaurant',)
        widgets = {
            'email' : EmailInput(attrs={
                'class': "input is-large", 
                'autofocus': '',
                'placeholder': 'Email'
                }),
            'restaurant': TextInput(attrs={
                'class': "input is-large",
                'autofocus': '',
                'placeholder': 'Restaurant\' Name'
                }),
            

        }
        
