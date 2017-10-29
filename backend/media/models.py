from django.db import models

class Media(models.Model):
    media_id = models.AutoField(primary_key=True)
    media_name = models.CharField(max_length=64, blank=False, null=False)
    media_type = models.CharField(max_length=1, blank=False, null=False)
    media_address = models.CharField(max_length=128, blank=False, null=True)
    