# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-04-17 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_auto_20190417_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='Address_info',
            field=models.TextField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='Contact',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
