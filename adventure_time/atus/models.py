from django.db import models

# Create your models here.


class Respondant(models.Model):
    case_id = models.CharField(max_length=14)


class Activity(models.Model):
    pass


class Household(models.Model):
    pass

