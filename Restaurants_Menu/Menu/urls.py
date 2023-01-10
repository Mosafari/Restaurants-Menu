from django.urls import path
from .views import SignUpView,LogInView, main

# adding paths
urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', LogInView.as_view(), name="login"),
    path('main/', main, name="main"),
    
]
