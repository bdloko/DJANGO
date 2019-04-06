from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

name_app = 'provider'

urlpatterns = [
        url(r'^dashboard/$', views.Accepted.as_view(), name='dashboard'),
        url(r'^provider_update/$', views.ProviderUpdate.as_view(), name='provider_update'),
        url(r'^providers/$', views.Providers.as_view(), name='providers'),
        url(r'^first_time/$', views.FirstTime.as_view(), name='first_time'),
        url(r'^register/$', views.Registration.as_view(), name='register'),
        url(r'^provider/$', views.CreateProvider.as_view(), name='provider'),
        url(r'^provider_profile/$', views.ProviderProfile.as_view(), name='provider_profile'),
        url(r'^home/$', views.Home.as_view(), name='home'),
        url(r'^login/$', views.Login.as_view(), name='login'),
        url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
        ]
