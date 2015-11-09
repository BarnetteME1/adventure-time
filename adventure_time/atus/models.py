from django.db import models

# Create your models here.
from django_filters import MethodFilter
import django_filters


class Respondant(models.Model):
    caseid = models.CharField(max_length=14)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.caseid


class Activity(models.Model):
    caseid = models.ForeignKey(Respondant)
    code = models.CharField(max_length=7)
    activity = models.CharField(max_length=82)
    weight = models.FloatField()
    minutesspend = models.IntegerField()

    def __str__(self):
        return self.activity


class Household(models.Model):
    caseid = models.ForeignKey(Respondant)
    location = models.IntegerField()
    houseincome = models.IntegerField()
    ownorrent = models.IntegerField()
    numberinhouse = models.IntegerField()
    highesteducation = models.IntegerField()
