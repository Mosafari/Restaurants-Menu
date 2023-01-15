from django.urls import path
from .views import SignUpView,LogInView, main, Logout, profile, home, AddToMenu, edit, AddAPI

# JWT token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# adding paths
urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', LogInView.as_view(), name="login"),
    path('main/', main, name="main"),
    path('logout/', Logout, name="logout"),
    path('profile/', profile, name="profile"),
    path('home/', home, name="home"),
    path('AddToMenu/', AddToMenu, name="add"),
    path('edit/', edit, name="updel"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/add/', AddAPI.as_view(), name="AddAPI"),
]
