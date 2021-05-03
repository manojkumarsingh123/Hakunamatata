# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-04-03 07:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0006_auto_20190403_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='Bookingdate',
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]