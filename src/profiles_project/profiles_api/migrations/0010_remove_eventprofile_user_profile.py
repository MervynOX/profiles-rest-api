# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-07-26 08:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0009_communityprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventprofile',
            name='user_profile',
        ),
    ]