from email.policy import default
# Create your models here.


from django.db import models

class Question (models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField("date de publication")

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerChoices(default=0)
