# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-10 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0003_eventprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventprofile',
            name='organiser_id',
            field=models.IntegerField(),
        ),
    ]
