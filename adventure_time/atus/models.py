from django.db import models

# Create your models here.


class Respondant(models.Model):
    caseid = models.CharField(max_length=14)
    peronlinenumber = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    activity = models.ManyToManyField()


class Activities(models.Model):
    code = models.IntegerField()
    weight = models.FloatField()
    title = models.CharField(max_length=50)
    minutesspend = models.IntegerField()


class Household(models.Model):
    caseid = models.ForeignKey(Respondant)
    personlinenumber = models.ForeignKey(Respondant)
    location = models.IntegerField()
    houseincome = models.IntegerField()
    ownorrent = models.IntegerField()
    numberinhouse = models.IntegerField()
    highesteducation = models.IntegerField()


class ActivityId(models.Model):
    activitycode = models.IntegerField()
    activity = models.CharField(max_limit=50)
