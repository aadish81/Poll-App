from django.db import models

# Create your models here.

class Question(models.Model):
    
    questions_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.questions_text
    
    
class Choice(models.Model):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='choices')
    chioce_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self): 
        return self.chioce_text