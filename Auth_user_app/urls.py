from django.urls import path
from . import views

urlpatterns = [
    path('', views.User_Signup, name='signup'),
    path('signup/', views.User_Signup, name='signup'),
    path('login/', views.User_login, name='login'),
    path('logout/', views.User_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
]


