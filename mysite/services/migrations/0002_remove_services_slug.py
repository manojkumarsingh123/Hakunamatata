# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-03-29 06:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='slug',
        ),
    ]