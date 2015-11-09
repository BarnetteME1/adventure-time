
from django.conf.urls import url
from atus_api.views import RespondantView, RespondantDetail, HouseholdView, HouseholdTwoView, ActivityList, \
    ActivityTwoList

urlpatterns = [
    url(r'^$', RespondantView.as_view(), name='respondant_api'),
    url(r'^(?P<caseid>\d+)/$', RespondantDetail.as_view(), name='respondant_detail_api'),
    url(r'household/$', HouseholdView.as_view(), name='household_api'),
    url(r'household/(?P<pk>.+)/$', HouseholdTwoView.as_view(), name='household_detail_api'),
    url(r'activity/$', ActivityList.as_view(), name='activity_detail_api'),
    url(r'activity/(?P<pk>.+)$', ActivityTwoList.as_view(), name='activity_detail_api')
]