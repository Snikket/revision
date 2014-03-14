from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Course(models.Model):
    #This field is required. Used to extend the OTB user object
    title = models.OneToOneField(User)
    lecturesLeft = models.DecimalField(max_digits=10, decimal_places=0)
    tutorialsLeft = models.DecimalField(max_digits=10, decimal_places=0)


class Lecture(models.Model):
    course = models.ForeignKey(Course)
    status = models.CharField(max_length=100)
    notes = models.CharField(max_length=1000)
    plannedCoverDate = models.DateTimeField(max_length=500)

class Tutorial(models.Model):
    course = models.ForeignKey(Course)
    status = models.CharField(max_length=100)

class TutorialQuestion(models.Model):
    tutorial = models.ForeignKey(Tutorial)
    status = models.CharField(max_length=100)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)

class Exam(models.Model):
    course = models.ForeignKey(Course)
    date = models.DateTimeField(max_length=500)
