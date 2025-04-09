from django.urls import path
from . import views


urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('ask/', views.ask_question, name='ask_question'),
    
]
