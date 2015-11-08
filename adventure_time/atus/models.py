from django.db import models

# Create your models here.


class Respondant(models.Model):
    caseid = models.CharField(max_length=14)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.caseid


class Activity(models.Model):
    caseid = models.ForeignKey(Respondant)
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

    def __str__(self):
        return str(self.caseid)

