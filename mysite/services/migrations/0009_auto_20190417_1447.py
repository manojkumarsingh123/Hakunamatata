# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-04-17 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20190417_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='Contact',
            field=models.CharField(max_length=10),
        ),
    ]
