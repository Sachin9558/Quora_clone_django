from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question
from answers.models import Answer

# Create your views here.

@login_required
def question_list(request):
    questions = Question.objects.all().order_by('-created_at')
    answers = Answer.objects.select_related('question', 'author').all().order_by('created_at') 
    print(answers)
    return render(request,"questions/question_list.html",{'questions':questions})

@login_required
def ask_question(request):
    if request.method =="POST":
        Question.objects.create(
            title=request.POST['title'],
            body=request.POST['body'],
            author = request.user
            
        )
        return redirect('question_list')
    return render(request, 'questions/ask_question.html')

