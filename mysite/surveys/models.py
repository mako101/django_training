from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(name='Question', max_length=200)
    pub_date = models.DateTimeField('Date Posted')

    def __str__(self):
        # As the name will be used as a column, have to use it for this method
        return self.Question


class Answer(models.Model):
    answer_text = models.CharField(name='Answer', max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        # As the name will be used as a column, have to use it for this method
        return self.Answer
