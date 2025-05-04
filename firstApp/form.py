from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Question , Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['questions_text','pub_date']
        widgets = {
                'questions_text': forms.TextInput(attrs= {
                    'class': 'w-full px-4 py-2 mb-8  rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400',
                    'placeholder': 'Enter the question'
                }),
                'pub_date': forms.TextInput(attrs=   {
                'class':'w-full px-4 py-2 rounded border border-gray-300 focus:outline-none  focus:ring-2 focus:ring-blue-400',
                'placeholder':'Enter Date',
                'type':'datetime-local'
            })
        }
class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['chioce_text']  
        widgets = {
            'chioce_text': forms.TextInput(attrs=   {
                'class':'w-full px-4 py-2 mb-8 rounded border border-gray-300 focus:outline-none  focus:ring-2 focus:ring-blue-400',
                'placeholder':'Enter options'
            })

        }      
        
ChoiceFormSet = inlineformset_factory(
    Question, Choice, 
    form=ChoiceForm , 
    fields= ['chioce_text'], 
    extra=3, 
    can_delete= False
    )
        
        
