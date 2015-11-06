from django.db import models

# Create your models here.


class Respondant(models.Model):
    case_id = models.CharField(max_length=14)
    weight = models.FloatField()
    age = models.IntegerField()
    sex = models.CharField(max_length=1)


class Activities(models.Model):
    case_id = models.ManyToMany(Respondant)


class Household(models.Model):
    pass


class ActivityCode(models.Model):
    code = models.IntegerField()
    title = models.CharField(max_length=50)
    average_minutes = models.IntegerField()
    total_respondants = models.IntegerField()
