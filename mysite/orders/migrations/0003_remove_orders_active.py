# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-04-02 19:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orders_bookingdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='active',
        ),
    ]
