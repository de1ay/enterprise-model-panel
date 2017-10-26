from django.db import models
from clients.models import Client

# TODO: Add relation with media
class Deal(models.Model):
    deal_id = models.AutoField(primary_key=True)
    deal_client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)
    deal_brand = models.CharField(max_length=64, null=False, blank=False)
    deal_sum = models.FloatField(null=False, blank=False)
    deal_type = models.CharField(max_length=1, null=False, blank=False)
    deal_time = models.FloatField(blank=False, null=False)
    deal_period = models.TextField(blank=False, null=False)
    deal_paid = models.FloatField()
