
from django.conf.urls import include, url
from atus_api.views import RespondantView, HouseholdDetail, ActivityDetail, RespondantDetail

urlpatterns = [
    url(r'^$', RespondantView.as_view(), name='respondant_api'),
    url(r'^(?P<pk>\d+)/$', RespondantDetail.as_view(), name='respondant_detail_api'),
    url(r'household/(?P<pk>\d+)/$', HouseholdDetail.as_view(), name='household_api'),
    url(r'activity/(?P<pk>\d+)/$', ActivityDetail.as_view(), name='activity_api')
]