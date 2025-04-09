from django.urls import path
from . import views

urlpatterns = [
    path('<int:question_id>/answer/', views.answer_questions, name='answer_question'),
    path('<int:answer_id>/like/', views.like_answer, name='like_answer'),
    path('answer/<int:answer_id>/like/', views.like_answer, name='like_answer'),
    path('answer/<int:answer_id>/dislike/', views.dislike_answer, name='dislike_answer'),
]
