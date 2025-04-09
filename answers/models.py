from django.db import models
from django.contrib.auth.models import User
from questions.models import Question

# Create your models here.

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    discription = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_answers',blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_answers', blank=True)
    
    def total_likes(self):
        return self.likes.count()
    
    def user_liked(self,user):
        return self.likes.filter(id=user.id).exists()
    
    def user_disliked(self,user):
        return self.dislikes.filter(id=user.id).exists()
    
    def __str__(self):
        return f"Answer to :{self.question.title}"