# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 23:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('billings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='billing_transfer_date',
            field=models.CharField(max_length=10),
        ),
    ]
