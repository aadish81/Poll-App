from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse , Http404
from .models import Question
from .models import Choice
from django.template import loader
from .form import QuestionForm , ChoiceFormSet,ChoiceForm



# Create your views here.
def Questions(request):
    questions = Question.objects.all()
    template = loader.get_template("index.html")
    context = {"questions":questions}
    return HttpResponse(template.render(context,request))

def Showchoices(request,id):
    question = Question.objects.get(id=id)
    Choices = question.choices.all()
    template = loader.get_template("choice.html")
    context = {"Choices":Choices,"Question":question}
    return HttpResponse(template.render(context,request))
    
def upVote(request,id):
    choice = Choice.objects.get(id=id)
    choice.votes += 1
    choice.save()
    question = choice.question  
    return redirect('firstapp:question', question.id)
    
def addPoll(request):
    
    if request.method == 'POST':
        questionform = QuestionForm(request.POST)
        
        if questionform.is_valid():
            question = questionform.save()
            formset = ChoiceFormSet(request.POST, instance=question)   
            if formset.is_valid():
                formset.save()
                return redirect('firstapp:questions')
            
    else:
        question_form = QuestionForm()
        formset= ChoiceFormSet()
        
    return render(request ,'addpoll.html',{'question_form':question_form,   'formset':formset})    
            
                     
def deleteQuestion(request,id):
    question = Question.objects.get(id = id)    
    question.delete()
    
    return redirect('firstapp:questions')
      
def editPoll(request,id):
    question = get_object_or_404(Question, pk = id)
    
    questionForm = QuestionForm(request.POST or None,instance=question)
    formset = ChoiceFormSet(request.POST or None, instance=question)
    if request.method == 'POST':
        if questionForm.is_valid() and formset.is_valid():
            questionForm.save()
            formset.save()
            return redirect('firstapp:questions')
        else:
            raise Http404('Question not found')

    return render(request, 'update.html' ,{"Question":questionForm, "Choices":formset})
        


