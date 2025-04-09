from django.shortcuts import render,redirect,get_object_or_404
from .models import Answer
from questions.models import Question
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def answer_questions(request,question_id):
    question = get_object_or_404(Question, id = question_id)
    if request.method == 'POST':
        Answer.objects.create(
            question = question,
            discription = request.POST['discription'],
            author = request.user           
            
        )
        return redirect('question_list')
    return render(request,"answers/answer_form.html",{'question':question})


@login_required
def like_answer(request,answer_id):
    answer = get_object_or_404(Answer,id = answer_id)
    user = request.user
    if answer.dislikes.filter(id=user.id).exists():
        answer.dislikes.remove(user)
    if answer.likes.filter(id = user.id).exists():
        answer.likes.remove(user)
    else:
        answer.likes.add(user)
    return redirect(request.META.get('HTTP_REFERER'))
    
    
@login_required
def dislike_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    user = request.user

    if answer.likes.filter(id=user.id).exists():
        answer.likes.remove(user)

    if answer.dislikes.filter(id=user.id).exists():
        answer.dislikes.remove(user)
    else:
        answer.dislikes.add(user)

    return redirect(request.META.get('HTTP_REFERER'))
        
