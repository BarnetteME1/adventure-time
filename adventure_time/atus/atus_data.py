from django.apps import apps
import pandas as pd
import atus
from atus.models import Respondant


def import_activity(apps, schema_editor):
    activity = pd.read_csv('~/my_projects/activity.csv')
    activity = activity[['TUCASEID', 'TUFINLWGT', 'variable', 'value']]
    Activity = apps.get_model('atus', 'Activity')
    for index, row in activity.iterrows():
        #caseid = row.TUCASEID
        weight = row.TUFINLWGT
        code = row.variable
        time = row.value
        Activity.objects.create(weight=weight, code=code, minutesspend=time)

def import_respondant(apps, schema_editor):
    data = pd.read_csv('~/iron_yard_hw/adventure-time/adventure_time/atus_data/data.csv')
    data = data[['TUCASEID', 'TULINENO', 'TEAGE', 'TESEX']]
    Respondants = apps.get_model('atus', 'Respondant')
    for index, row in data.iterrows():
        caseid = row.TUCASEID
        peronlinenumber = row.TULINENO
        age = row.TEAGE
        gender = row.TESEX
        Respondants.objects.create(caseid=caseid, peronlinenumber=peronlinenumber, age=age, gender=gender)

def import_household(apps, schema_editor):
    household = pd.read_csv('~/iron_yard_hw/adventure-time/adventure_time/atus_data/household.csv')
    household = household[['TUCASEID', 'TULINENO', 'GEDIV', 'HEFAMINC', 'HETENURE', 'HRNUMHOU', 'PEEDUCA']]
    Household = apps.get_model('atus', 'Household')
    for index, row in household.iterrows():
        location = row.GEDIV
        houseincome = row.HEFAMINC
        ownorrent = row.HETENURE
        numberinhouse = row.HRNUMHOU
        highesteducation = row.PEEDUCA
        Household.objects.create(location=location, houseincome=houseincome, ownorrent=ownorrent, numberinhouse=numberinhouse, highesteducation=highesteducation)