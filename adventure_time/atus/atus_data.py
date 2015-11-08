from django.apps import apps
import pandas as pd
import atus
from atus.models import Respondant


def import_activity(apps, schema_editor):
    activity = pd.read_csv('~/my_projects/activity.csv')
    activity = activity[['TUCASEID', 'TUFINLWGT', 'variable', 'value']]
    Respondant = apps.get_model('atus', 'Respondant')
    Activity = apps.get_model('atus', 'Activity')
    for index, row in activity.iterrows():
        caseid = row.TUCASEID
        weight = row.TUFINLWGT
        code = row.variable
        time = row.value
        Activity.objects.create(caseid=Respondant.objects.get(caseid=caseid), weight=weight, activity=code, minutesspend=time)


def import_respondant(apps, schema_editor):
    data = pd.read_csv('~/my_projects/data.csv')
    data = data[['TUCASEID', 'TEAGE', 'TESEX']]
    Respondant = apps.get_model('atus', 'Respondant')
    for index, row in data.iterrows():
        caseid = row.TUCASEID
        age = row.TEAGE
        gender = row.TESEX
        Respondant.objects.create(caseid=caseid, age=age, gender=gender)


def import_household(apps, schema_editor):
    household = pd.read_csv('~/my_projects/household.csv')
    household = household[['TUCASEID', 'GEDIV', 'HEFAMINC', 'HETENURE', 'HRNUMHOU', 'PEEDUCA']]
    Household = apps.get_model('atus', 'Household')
    Respondant = apps.get_model('atus', 'Respondant')
    for index, row in household.iterrows():
        caseid = row.TUCASEID
        location = row.GEDIV
        houseincome = row.HEFAMINC
        ownorrent = row.HETENURE
        numberinhouse = row.HRNUMHOU
        highesteducation = row.PEEDUCA
        Household.objects.create(caseid=Respondant.objects.get(caseid=caseid), location=location, houseincome=houseincome, ownorrent=ownorrent, numberinhouse=numberinhouse, highesteducation=highesteducation)
