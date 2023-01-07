from django.urls import path
from .views import SignUpView

# adding paths
urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),

    
]
