from django.db import models
from deals.models import Deal


class Billing(models.Model):
    billing_id = models.AutoField(primary_key=True)
    billing_deal = models.ForeignKey(Deal, on_delete=models.CASCADE, blank=False)
    billing_sum = models.IntegerField(blank=False, null=False)
    billing_date = models.CharField(max_length=10, null=False, blank=False)
    billing_transfer_date = models.CharField(max_length=10, null=False, blank=False)

    def update_related_deal (self, original_billing_sum, original_related_deal):
        new_related_deal = self.billing_deal
        if new_related_deal.deal_id != original_related_deal.deal_id:
            original_related_deal.change_paid_value(original_billing_sum * -1)
            new_related_deal.change_paid_value(self.billing_sum)
        else:
            new_related_deal.change_paid_value(self.billing_sum - original_billing_sum)