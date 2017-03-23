import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


# create database fields for the Question model
@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# string method for clear, readable object representation in admin
    def __str__(self):
        return self.question_text

# method indicates whether poll was published recently (within the last 24 hours)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# create database fields for the Choice model
@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# string method for clear, readable object representation in admin
    def __str__(self):
        return self.choice_text
