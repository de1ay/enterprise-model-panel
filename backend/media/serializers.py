from .models import Media
from rest_framework import serializers

class MediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        fields = ('media_id', 
        'media_name', 
        'media_type',
        'media_address',)