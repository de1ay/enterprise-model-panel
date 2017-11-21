from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BillingsAPI
from .views import BillingAPI

urlpatterns = [
    url(r'^$', BillingsAPI.as_view()),
    url(r'^(?P<id>[0-9]+)$', BillingAPI.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)