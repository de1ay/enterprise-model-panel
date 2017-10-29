from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ClientsAPI
from .views import ClientAPI

urlpatterns = [
    url(r'^$', ClientsAPI.as_view()),
    url(r'^(?P<id>[0-9]+)/$', ClientAPI.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)