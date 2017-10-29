from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MediaAPI
from .views import MediaDetailedAPI

urlpatterns = [
    url(r'^$', MediaAPI.as_view()),
    url(r'^(?P<id>[0-9]+)/$', MediaDetailedAPI.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)