from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('add_Question/<str:pk>/',views.addQuestion,name='addquestion'),
    path('question/',views.userQuestions,name='userquestions'),
    path('question/<str:pk>/',views.loadQuestion,name='question'),
    path('editquestion/<str:pk>/',views.editQuestion,name='editquestion'),
    path('deletequestion/<str:pk>/',views.deleteQuestion,name='deletequestion'),
]