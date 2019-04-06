from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^django_popup_view_field/', include('django_popup_view_field.urls', namespace="django_popup_view_field")),
#    url(r'^search/', include('haystack.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url('admin/', admin.site.urls),
    url('', include('provider.urls')),
    url('', include('requester.urls')),
    url(r'^$', TemplateView.as_view(template_name='provider/home.html'), name="home"),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
