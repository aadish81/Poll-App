from django.shortcuts import render
from firstApp.models import Question , Choice
from django.http import HttpResponse



# Create your views here.

def Questions(request):
    questions = Question.objects.all()
    output = ",".join([q.questions_text for q in questions])
    return HttpResponse(output)                     