# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-27 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0002_deal_deal_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='deal_status',
            field=models.CharField(default='0', max_length=1),
        ),
    ]