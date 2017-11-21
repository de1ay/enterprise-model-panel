from .models import Deal
from rest_framework import serializers
from clients.models import Client
from media.models import Media

class DealSerializer(serializers.ModelSerializer):
    deal_client = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Client.objects.all())
    deal_media = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Media.objects.all())

    class Meta:
        model = Deal
        fields = ('deal_id', 
        'deal_client', 
        'deal_brand',
        'deal_media', 
        'deal_sum', 
        'deal_time',
        'deal_type',
        'deal_period',
        'deal_paid',
        'deal_status')