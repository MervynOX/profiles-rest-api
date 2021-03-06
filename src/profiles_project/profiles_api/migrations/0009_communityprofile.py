# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-07-13 05:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0008_eventprofile_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=5000)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
