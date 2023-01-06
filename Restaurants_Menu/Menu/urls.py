from django.urls import path
from . import views

# adding paths
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    # path('menus/', views),
    
]
