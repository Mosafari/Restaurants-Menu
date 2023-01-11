from django.urls import path
from .views import SignUpView,LogInView, main, Logout, profile, home

# adding paths
urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', LogInView.as_view(), name="login"),
    path('main/', main, name="main"),
    path('logout/', Logout, name="logout"),
    path('profile/', profile, name="profile"),
    path('home/', home, name="home"),
    
]
