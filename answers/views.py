from datetime import datetime, timedelta
from email import message
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .models import *
from .forms import questionForm
from django.core import serializers
# Create your views here.
def main(request):
    # allQuestions = questions.objects.all()
    # order by vote
    if request.method == 'POST':
        title = request.POST['title']
        squestion = questions.objects.filter(title__icontains=title)
        squestion = serializers.serialize('json', squestion)
        return JsonResponse({'questions':squestion})
    # squestions = questions.objects.filter(time__gt = datetime.now() - timedelta(days=100))[0:30]
    # squestions = questions.objects.filter(answered=False)[0:30]
    squestions = questions.objects.all()
    context = {'questions':squestions}
    return render(request,'main.html',context)

@login_required(login_url='login')
def addQuestion(request,pk):
    if request.method == 'POST':
        questioner = User.objects.get(id=pk)
        if request.FILES:
            newquestion = questions.objects.create(
            questioner=questioner,
            title = request.POST['title'],
            question_image = request.FILES['question_image']
                )
        else:
            newquestion = questions.objects.create(
            questioner=questioner,
            title = request.POST['title'],
            )
        messages.info(request,'Question Added Succesfully')
        return redirect('main')    
    return render(request,'main.html')


def loadQuestion(request,pk):
    question = questions.objects.get(id=pk)
    sanswers = answers.objects.filter(question=question)
    if request.method == 'POST':
        answerer = User.objects.get(id=request.POST['userid'])
        if request.FILES:
            newanswer = answers.objects.create(
            answerer = answerer,
            question=question,
            answer = request.POST['answer'],
            answer_image=request.FILES['answer_image']
            )
        else:
            newanswer = answers.objects.create(
                answerer = answerer,
                question=question,
                answer = request.POST['answer']
            )
        messages.info(request,'Answer Added Succesfully')
        return HttpResponseRedirect(request.path_info)
    context={'question':question,'answers':sanswers}
    print(request.path_info)
    return render(request,'answers/question.html',context)



@login_required(login_url='login')
def userQuestions(request):
    user = User.objects.get(id=request.user.id)
    userquestions = questions.objects.filter(questioner=user)
    context={'questions':userquestions}
    return render(request,'answers/userquestion.html',context)


@login_required(login_url='login')
def editQuestion(request,pk):
    question = questions.objects.get(id=pk)
    form = questionForm(instance=question)
    if request.method == 'POST':
        editedquestion = questionForm(request.POST,request.FILES,instance=question)
        if editedquestion.is_valid():
            editedquestion.save()
            return redirect('userquestions')
    context={'form':form,'question':question}
    return render(request,'answers/editquestion.html',context)

@login_required(login_url='login')
def deleteQuestion(request,pk):
    question = questions.objects.get(id=pk)
    question.delete()
    messages.info(request,'Question deleted succesfully')
    return redirect('userquestions')