from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UsersAPI
from .views import UserAPI

urlpatterns = [
    url(r'^$', UsersAPI.as_view()),
    url(r'^(?P<id>[0-9]+)$', UserAPI.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)