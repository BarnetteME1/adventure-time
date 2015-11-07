from django.apps import apps
import pandas as pd
import atus
from atus.models import Respondant


def import_activity(apps, schema_editor):
    activity = pd.read_csv('~/iron_yard_hw/adventure-time/adventure_time/atus_data/activity.csv')
    activity = activity[['TUCASEID', 'TUFINLWGT', 'variable', 'value']]
    one_to_one = pd.read_csv('~/iron_yard_hw/adventure-time/adventure_time/atus_data/activity.csv')
    one_to_one = one_to_one[['6-digit activity code', 'Activity']]
    Activity = apps.get_model('Activity')

def import_respondant(apps, schema_editor):
    data = pd.read_csv('~/iron_yard_hw/adventure-time/adventure_time/atus_data/data.csv', header=0)
    data = data[['TUCASEID', 'TULINENO', 'TEAGE', 'TESEX']]
    Respondant = apps.get_models('atus', 'Respondant')
    for index, row in data.iterrows():
        caseid = row.TUCASEID
        peronlinenumber = row.TULINENO
        age = row.TEAGE
        gender = row.TESEX
        Respondant.objects.create(caseid=caseid, peronlinenumber=peronlinenumber, age=age, gender=gender)

def import_household(apps, schema_editor):
    household = pd.read_csv('~/iron_yard_hw/adventure-time/adventure_time/atus_data/household.csv')
    household = household[['TUCASEID', 'TULINENO', 'GEDIV', 'HEFAMINC', 'HETENURE', 'HRNUMHOU', 'PEEDUCA']]
    Household = apps.get_model('Household')