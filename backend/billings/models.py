from django.db import models
from deals.models import Deal


class Billing(models.Model):
    billing_id = models.AutoField(primary_key=True)
    billing_deal = models.ForeignKey(Deal, on_delete=models.CASCADE, blank=False)
    billing_sum = models.IntegerField(blank=False, null=False)
    billing_date = models.CharField(max_length=10, null=False, blank=False)
    billing_transfer_date = models.CharField(max_length=10, null=False, blank=False)