from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import ListView
import django_filters
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.serializers import ModelSerializer
from atus.models import Respondant, Activity, Household


class RespondantSerializer(ModelSerializer):

    class Meta:
        model=Respondant
        lookup_field = 'caseid'

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
    lookup_field = 'caseid'

class ActivityList(ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityTwoList(ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):
        activity = self.kwargs['pk']
        return Household.objects.filter(activity=activity)

class HouseholdView(ListAPIView):
    queryset = Household.objects.all()
    serializer_class = HouseholdSerializer

class HouseholdTwoView(ListAPIView):
    queryset = Household.objects.all()
    serializer_class = HouseholdSerializer

    def get_queryset(self):
        caseid = self.kwargs['pk']
        return Household.objects.filter(caseid=caseid)

class HouseholdDetail(RetrieveAPIView):
    serializer_class = HouseholdSerializer
