from  django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('goodbye/', views.say_goodbye),
    path('questions/', views.Questions),
    path('question/<int:id>/',views.Showchoices),
    path('choice/<int:id>/', views.upVote),
    path('', views.home)
    
]