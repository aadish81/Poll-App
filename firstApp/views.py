from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.http import JsonResponse
from .models import Question
from .models import Choice
from django.template import loader

# Create your views here.
def say_hello(request):
    return HttpResponse("<h1>Hello World</h1>")

def say_goodbye(request):
    return HttpResponse("<h2>Good Bye sweety</h2>")

def Questions(request):
    questions = Question.objects.all()
    template = loader.get_template("firstApp/index.html")
    context = {"questions":questions}
    return HttpResponse(template.render(context,request))

def Showchoices(request,id):
    question = Question.objects.get(id=id)
    Choices = question.choices.all()
    template = loader.get_template("firstApp/choice.html")
    context = {"Choices":Choices,"Question":question}
    return HttpResponse(template.render(context,request))
    
def upVote(request,id):
    choice = Choice.objects.get(id=id)
    choice.votes += 1
    choice.save()  
    question = choice.question
    Choices = question.choices.all()
    template = loader.get_template("firstApp/choice.html")
    Context = {"Choices":Choices,"Question":question}
    return HttpResponse(template.render(Context,request))
    
def home(request):
    return render(request,'base.html')