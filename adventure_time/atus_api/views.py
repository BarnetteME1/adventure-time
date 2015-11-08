from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.serializers import ModelSerializer
from atus.models import Respondant, Activity, Household


class RespondantSerializer(ModelSerializer):

    class Meta:
        model=Respondant

class ActivitySerializer(ModelSerializer):

    class Meta:
        model=Activity

class HouseholdSerializer(ModelSerializer):

    class Meta:
        model=Household

class RespondantView(ListAPIView):
    queryset = Respondant.objects.all()
    serializer_class = RespondantSerializer

class RespondantDetail(RetrieveAPIView):
    queryset = Respondant.objects.all()
    serializer_class = RespondantSerializer

class ActivityDetail(RetrieveAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class HouseholdDetail(RetrieveAPIView):
    queryset = Household.objects.all()
    serializer_class = HouseholdSerializer