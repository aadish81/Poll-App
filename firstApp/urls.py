from  django.urls import path
from . import views


app_name = 'firstapp'

urlpatterns = [

    path('questions/', views.Questions, name='questions'),
    path('question/<int:id>/',views.Showchoices, name='question'),
    path('choice/<int:id>/', views.upVote, name = 'choice'),
    path('addpoll/',views.addPoll,name='addpoll'),
    path('delete/<int:id>/', views.deleteQuestion, name = 'delete'),
    path('editpoll/<int:id>/', views.editPoll, name='editpoll')
]
