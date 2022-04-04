from turtle import title
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
# Create your models here.
class questions(models.Model):
    questioner = models.ForeignKey(User,null=True,blank=False,on_delete=models.SET_NULL)
    title = models.CharField(max_length=10000,null=False,blank=False)
    question_image = models.ImageField(null=True,blank=True,upload_to='question_image')
    # time = models.DateTimeField(default=datetime.now,blank=False)
    time = models.DateTimeField(auto_now_add=True)
    answered = models.BooleanField(default=False) 

    def __str__(self):
        return self.title

class answers(models.Model):
    answerer = models.ForeignKey(User,null=True,blank=False,on_delete=models.SET_NULL)
    question = models.ForeignKey(questions,null=True,blank=False,on_delete=models.SET_NULL)
    answer = models.TextField()
    answer_image = models.ImageField(null=True,blank=True,upload_to='answer_image')
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.question.title

def answered(sender,instance,created,**kwargs):
    id = instance.question.id
    questiond = questions.objects.get(id=id)
    questiond.answered = True
    questiond.save()

post_save.connect(answered,sender=answers)