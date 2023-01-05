from django.urls import path
from . import views

# adding paths
urlpatterns = [
    path('login/', views),
    path('signup/', views),
    path('menus/', views),
    
]
