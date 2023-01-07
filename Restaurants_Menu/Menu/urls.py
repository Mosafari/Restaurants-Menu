from django.urls import path
from . import views

# adding paths
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('api/register/', views.RegisterView.as_view(), name="sign_up"),
    # path('menus/', views),
    
]
