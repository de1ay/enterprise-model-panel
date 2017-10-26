from .models import Deal
from rest_framework import serializers

class DealSerializer(serializers.ModelSerializer):
    deal_client = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Deal
        fields = ('deal_id', 
        'deal_client', 
        'deal_brand', 
        'deal_sum', 
        'deal_type', 
        'deal_time', 
        'deal_period',
        'deal_paid')