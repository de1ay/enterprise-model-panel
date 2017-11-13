from .models import Billing
from rest_framework import serializers
from deals.models import Deal

class BillingSerializer(serializers.ModelSerializer):
    billing_deal = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Deal.objects.all())

    class Meta:
        model = Billing
        fields = ('billing_id',
        'billing_deal',
        'billing_sum',
        'billing_date')