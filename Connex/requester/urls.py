from django.conf.urls import url, include
from . import views

name_app = 'requester'

urlpatterns = [
        url(r'^requesters/$', views.Requesters.as_view(), name='requesters'),
        url(r'^requester/$', views.CreateRequester.as_view(), name='requester'),
        url(r'^requester_profile/$', views.RequesterProfile.as_view(), name='requester_profile'),
        url(r'^challenge/category/(?P<pk>[\d]+)/$', views.ChallengeCategory.as_view(), name='challenge_category'),
        url(r'^challenger/$', views.Challenger.as_view(), name='challenger'),
        url(r'^challenge/(?P<pk>[\d]+)/delete/$', views.ChallengeDelete.as_view(), name='challenge_delete'),
        url(r'^challenge/(?P<pk>[\d]+)/update/$', views.ChallengeUpdate.as_view(), name='challenge_update'),
        url(r'^challenge/add/$', views.ChallengeCreate.as_view(), name='challenges_create'),
        url(r'^challenge/(?P<pk>[\d]+)/dates/$', views.ChallengeDates.as_view(), name='challenges_dates'),
        url(r'^challenge/(?P<pk>[\d]+)/$', views.ChallengeDetail.as_view(), name='challenge_detail'),
        url(r'^challenges/$', views.Challenges.as_view(), name='challenges'),
        ]