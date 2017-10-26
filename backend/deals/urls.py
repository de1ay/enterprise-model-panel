from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DealsAPI
from .views import DealAPI

urlpatterns = [
    url(r'^$', DealsAPI.as_view()),
    url(r'^(?P<id>[0-9]+)/$', DealAPI.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)