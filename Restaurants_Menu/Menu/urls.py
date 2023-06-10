from django.urls import path, re_path
from .views import SignUpView,LogInView, main, Logout, profile, home, AddToMenu, edit, AddAPI, APIMenu, loginredirect

# JWT token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# adding paths
urlpatterns = [
    re_path('^(?=\s*$)', loginredirect, name="logredirect"),
    path('restaurant/signup/', SignUpView.as_view(), name="signup"),
    path('restaurant/login/', LogInView.as_view(), name="login"),
    path('restaurant/main/', main, name="main"),
    path('restaurant/logout/', Logout, name="logout"),
    path('restaurant/profile/', profile, name="profile"),
    path('restaurant/home/', home, name="home"),
    path('restaurant/AddToMenu/', AddToMenu, name="add"),
    path('restaurant/edit/', edit, name="updel"),
    path('restaurant/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('restaurant/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('restaurant/api/add/', AddAPI.as_view(), name="AddAPI"),
    path('restaurant/api/menu/', APIMenu.as_view(), name="APIMenu"),
    
]
